var gulp = require('gulp'),
    connect = require('gulp-connect');

gulp.task('connect',function(){
    connect.server({
        root: './',
        livereload: true
    });
});
gulp.task('html',function(){
    gulp.src('html/*.html')
        .pipe(connect.reload());
});

gulp.task('watch',function(){
    gulp.watch(['html/*.html','css/*.css','js/*.js'],['html']);
});

gulp.task('default',['connect','watch']);
