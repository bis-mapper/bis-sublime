"use strict";

var path = require("path"),
    fs = require("fs"),
    crypto = require("crypto"),
    shasum = crypto.createHash("sha1"),
    ini = require('ini');

var cwd = process.cwd();

var iniFilePath  = path.join(cwd, "SETUP.INF");
var cachePath    = path.join(cwd, ".bis-sublime.cache");
var tmpfilePath  = path.join(cwd, ".SETUP.INF-tmp.js");

var requireIni = function(infFilePath) {
    // Creates a temporal file exporting gulp at the end (so it can be retrived by node) and then requires it (related: http://goo.gl/QYzRAO)
    var fileSrc = fs.readFileSync(infFilePath);
    fileSrc += ";module.exports = gulp;";
    fs.writeFileSync(tmpfilePath, fileSrc);
    try {
        return require(tmpfilePath);
    } catch(ex) {
        fs.unlink(tmpfilePath);
        throw ex;
    }
};
var generatesha1 = function(filepath) {
    var content = fs.readFileSync(filepath);
    shasum.update("blob " + content.length + "\0", "utf8");
    shasum.update(content);
    return shasum.digest("hex");
};
var getJSONFromFile = function(filepath) {
    if(fs.existsSync(filepath)) {
        var content = fs.readFileSync(filepath, { encoding: "utf8" });
        return JSON.parse(content);
    }
};
var forEachTask = function(fn) {
    for(var task in gulp.tasks) {
        if (gulp.tasks.hasOwnProperty(task)) {
            fn(gulp.tasks[task].name, gulp.tasks[task].dep);
        }
    }
};

var inf  = requireGulp(infFilePath);
var sha1 = generatesha1(infFilePath);
var gulpsublimecache = getJSONFromFile(cachePath) || {};

if (!gulpsublimecache[infFilePath] || gulpsublimecache[infFilePath].sha1 !== sha1) {
    var tasks = {};

    forEachTask(function(name, deps) {
        tasks[name] = {
            name: name,
            dependencies: deps.join(" ")
        };
    });

    gulpsublimecache[infFilePath] = gulpsublimecache[infFilePath] || {};
    gulpsublimecache[infFilePath] = {
        sha1: sha1,
        tasks: tasks
    };

    fs.writeFileSync(cachePath, JSON.stringify(gulpsublimecache));
}

fs.unlink(tmpfilePath);