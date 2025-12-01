window.addEventListener("DOMContentLoaded", function () {
    if (window.MathJax) {
        MathJax.typesetPromise().then(() => {
            console.log("MathJax equations rendered.");
        }).catch((err) => console.error("MathJax error:", err));
    } else {
        console.error("MathJax not loaded.");
    }
});