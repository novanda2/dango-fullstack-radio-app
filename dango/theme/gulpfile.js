const __prod__ = process.env.NODE_ENV === 'production'
const { src, dest, watch, series, parallel } = require('gulp')

const noop = require('gulp-noop')
const concat = require('gulp-concat')

const sass = require('gulp-sass')(require('node-sass'))
const postcss = require('gulp-postcss')
const cleanCSS = require('gulp-clean-css')
const autoprefixer = require('gulp-autoprefixer')

const _styles = (cb) => {
	src("./src/styles/index.scss")
		.pipe(
			sass({ outputStyle: 'compressed' }).on('error', sass.logError)
		)
		.pipe(postcss())
		.pipe(
			autoprefixer({
				browserlist: ['last 2 versions'],
				cascade: false
			})
		)
		.pipe(__prod__ ? cleanCSS({ compatibility: 'ie8' }) : noop())
		.pipe(concat("styles.css"))
		.pipe(dest('../static/theme'))
	cb()
}

const _watch = (cb) => {
	watch("./**/*.scss", _styles)
	cb()
}

exports.default = series(_styles, _watch)
exports.build = parallel(_styles)

