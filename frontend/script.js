



async function generateReply() {
  const email = document.getElementById('emailInput').value.trim();
  const tone = document.getElementById('toneSelect').value;
  const outputDiv = document.getElementById('output');
  const loading = document.getElementById('loading');
  const copyBtn = document.getElementById('copyBtn');

  outputDiv.innerText = "";
  copyBtn.classList.add('hidden');
  loading.classList.remove("hidden");

  try {
    const response = await fetch("http://127.0.0.1:8000/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ email, tone })
    });

    const data = await response.json();
    outputDiv.innerText = data.reply;

    if (data.reply && data.reply.trim() !== "") {
      copyBtn.classList.remove('hidden');
    }
  } catch (error) {
    console.error(error);
    outputDiv.innerText = "❌ Error generating reply. Please check backend or internet.";
  } finally {
    loading.classList.add("hidden");
  }
}

function copyReply() {
  const outputDiv = document.getElementById('output');
  const text = outputDiv.innerText;

  if (!text) return;

  navigator.clipboard.writeText(text).then(() => {
    alert("Reply copied to clipboard!");
  }).catch(() => {
    alert("Failed to copy. Please copy manually.");
  });
}
