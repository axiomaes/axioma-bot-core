/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            colors: {
                primary: "#E63946",
                secondary: "#457B9D",
                accent: "#A8DADC",
                background: "#1A1A1A",
                light: "#F1FAEE",
            }
        },
    },
    plugins: [],
}
