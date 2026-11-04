const startButton = document.querySelector("#start");
const messages = document.querySelector("#messages");

function addMessage(text, role) {
  const bubble = document.createElement("div");
  bubble.className = `bubble ${role}`;
  bubble.textContent = text;
  messages.appendChild(bubble);
  messages.scrollTop = messages.scrollHeight;
}

startButton.addEventListener("click", async () => {
  const destination = document.querySelector("#destination").value;
  const budget = document.querySelector("#budget").value;
  const days = document.querySelector("#days").value;

  if (budget === "" || Number(budget) < 0) {
    addMessage("予算を0以上の数字で入力してください。", "bot");
    return;
  }

  addMessage(`${destination}に行きたい！予算は${Number(budget).toLocaleString()}円、${days}日間。`, "user");
  startButton.disabled = true;
  startButton.textContent = "プランを考えています…";

  try {
    const response = await fetch("/api/chat", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({destination, budget, days})
    });
    const data = await response.json();
    addMessage(data.reply || "プランを作成できませんでした。", "bot");
  } catch (error) {
    addMessage("通信に失敗しました。ページを更新してもう一度お試しください。", "bot");
  } finally {
    startButton.disabled = false;
    startButton.innerHTML = 'プランを相談する <span>→</span>';
  }
});
