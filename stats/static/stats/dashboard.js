// Get the 'dashboardSlug' from the HTML element with the ID 'dashboard-slug'.
const dashboardSlug = document
  .getElementById("dashboard-slug")
  .textContent.trim();

// Create a WebSocket connection to the server using the obtained 'dashboardSlug'.
const socket = new WebSocket(
  `ws://${window.location.host}/ws/${dashboardSlug}/`
);

console.log(socket);

// This function is called when the WebSocket connection is successfully opened.
socket.onopen = function (e) {
  console.log("Chat socket opened");

  // Send a JSON message to the server once the connection is open.
  socket.send(
    JSON.stringify({ message: "Hello from the client!", sender: "test-client" })
  );
};

// This function is called when a message is received from the server.
socket.onmessage = function (e) {
  // Parse the received JSON data into a JavaScript object.
  const data = JSON.parse(e.data);

  // Log the received data from the server for debugging purposes.
  console.log("Server: ", data);
};

// This function is called when the WebSocket connection is closed unexpectedly.
socket.onclose = function (e) {
  console.error("Chat socket closed unexpectedly");
};
