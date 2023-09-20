const dashboardSlug = document
  .getElementById("dashboard-slug")
  .textContent.trim();
console.log("dashboardSlug: ", dashboardSlug);

const socket = new WebSocket(
  `ws://${window.location.host}/ws/${dashboardSlug}/`
);
console.log(socket);

socket.onopen = function (e) {
  console.log("Chat socket opened");
  socket.send(
    JSON.stringify({ message: "Hello from the client!", sender: "test-client" })
  );
};

socket.onmessage = function (e) {
  const data = JSON.parse(e.data);
  console.log("Server: ", data);
};

socket.onclose = function (e) {
  console.error("Chat socket closed unexpectedly");
};
