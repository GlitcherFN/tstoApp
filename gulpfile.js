'use strict';

var gulp = require('gulp');
var _$ = require('gulp-load-plugins')();

gulp.task('stylus', function() {
  gulp.src('./core/vendor/css/estilos.styl')
    .pipe(_$.stylus())
    .pipe(gulp.dest('./core/static/css/'));
});

/**
 * Watch File
 */
gulp.task('watch', function() {
  gulp.watch('./core/vendor/css/*.styl', ['stylus']);
});

gulp.task('default', ['watch']);
