const video = document.getElementById('video');
const resultsDiv = document.getElementById('results');
const ws = new WebSocket('ws://localhost:8000/ws');

ws.onmessage = function(event) {
    const data = JSON.parse(event.data);
    resultsDiv.innerHTML = `
        <h2>Detected Mood: ${data.emotion}</h2>
        <a href="${data.playlist_url}" target="_blank">Play Recommended Playlist</a>
    `;
};

navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => video.srcObject = stream);