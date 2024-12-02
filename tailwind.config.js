/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.{html,js}", // Direktori template Django
    "./**/templates/**/*.html", // Jika menggunakan aplikasi Django terpisah
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
