async function generateReply() {
  const email = document.getElementById('emailInput').value.trim();
  const tone = document.getElementById('toneSelect').value;
  const outputDiv = document.getElementById('output');
  const loading = document.getElementById('loading');
  const copyBtn = document.getElementById('copyBtn');
  const subjectInput = document.getElementById('subjectLine');

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

    // Separate first line as subject, rest as body
    const lines = data.reply.split('\n').filter(line => line.trim() !== '');

    let subjectLine = "";
    let bodyText = "";

    if (lines.length > 1) {
      subjectLine = lines[0].trim(); // first line as subject
      bodyText = lines.slice(1).join('\n').trim(); // rest as body
    } else {
      subjectLine = "";
      bodyText = data.reply.trim();
    }

    subjectInput.value = subjectLine;
    outputDiv.innerText = bodyText;

    if (bodyText) {
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

async function sendReply() {
  const toEmail = document.getElementById('toEmail').value.trim();
  const subject = document.getElementById('subjectLine').value.trim();
  const body = document.getElementById('output').innerText.trim();
  const statusDiv = document.getElementById('emailStatus');
  const sendLoading = document.getElementById('sendLoading');

  if (!toEmail || !subject || !body) {
    alert("All fields are required!");
    return;
  }

  statusDiv.innerText = "";
  sendLoading.classList.remove('hidden');

  try {
    const response = await fetch("http://127.0.0.1:8000/send-email", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ to_email: toEmail, subject, body })
    });

    const data = await response.json();
    statusDiv.innerText = data.message;
  } catch (error) {
    console.error("Sending error:", error);
    statusDiv.innerText = "❌ Failed to send email.";
  } finally {
    sendLoading.classList.add('hidden');
  }
}
