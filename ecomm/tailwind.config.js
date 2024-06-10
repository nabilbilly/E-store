/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../template/**/*.{html,js}",
    '../template/**/*.html',           // Project-wide templates
    './template/**/*.html',  
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

