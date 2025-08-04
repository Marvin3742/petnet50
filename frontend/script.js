const classifyButton = document.getElementById("classifyButton");

classifyButton.addEventListener("click", async () => {
  const input = document.getElementById("inputImage");
  const output = document.getElementById("modelOutput");

  const file = input.files[0];
  if (!file) {
    output.innerText = "Please upload an image.";
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  output.innerText = "Predicting...";

  try {
    const res = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    output.innerText = data.prediction
      ? `Prediction: ${data.prediction}`
      : `Error: ${data.error || "Unknown error"}`;
  } catch (err) {
    output.innerText = "Prediction failed. Is the backend running?";
  }
});
