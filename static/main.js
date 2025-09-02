document.addEventListener("DOMContentLoaded", () => {
  const buttons = document.querySelectorAll(".mood-btn");
  const quoteEl = document.getElementById("quote");
  const resultWrapper = document.getElementById("result");
  const errorEl = document.getElementById("error");

  buttons.forEach((btn) => {
    btn.addEventListener("click", async () => {
      const mood = btn.dataset.mood;
      errorEl.textContent = "";
      quoteEl.textContent = "Loading...";
      resultWrapper.classList.remove("hidden");

      try {
        const response = await fetch("/get_mood", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ mood }),
        });
        const data = await response.json();
        quoteEl.textContent = data.quote;
        if (data.error) {
          console.warn(data.error);
        }
      } catch (err) {
        resultWrapper.classList.add("hidden");
        errorEl.textContent = "Oops! Something went wrong. Please try again.";
        console.error(err);
      }
    });
  });
});
