'use strict';

var fs = require('fs');
var gulp = require('gulp');
var _$ = require('gulp-load-plugins')();
var lines = [];
var newFile = null;

gulp.task('stylus', function() {
  gulp.src('./core/vendor/css/estilos.styl')
    .pipe(_$.stylus())
    .pipe(gulp.dest('./core/static/css/'));
});

gulp.task('submodule', function() {
    var file = fs.readFileSync('./core/vendor/tsto/tsto.py', {encoding: 'utf-8'});
    lines = file.split('\n');
    lines[949] = "'''"
    lines[lines.length - 1] = "'''";
    newFile = lines.join('\n');
    fs.writeFile('./core/vendor/tsto/tsto.py', newFile, function(err) {
      if (err) { throw err; }
    });
});

/**
 * Watch File
 */
gulp.task('watch', function() {
  gulp.watch('./core/vendor/css/*.styl', ['stylus']);
});

gulp.task('default', ['watch']);
