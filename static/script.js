let context = new (window.AudioContext || window.webkitAudioContext)();

document.getElementById('sepsis-form').addEventListener('submit', function(event) {
    event.preventDefault();

    let formData = new FormData(this);

    fetch('/predict/patient', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        const resultContainer = document.getElementById('result-container');

        if (data.Prediction === 1) {
            resultContainer.textContent = "Positif";
            resultContainer.style.color = 'red';
        } else {
            resultContainer.textContent = "Négatif";
            resultContainer.style.color = 'green';
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

function initForm() {
    let url = '/static/cache/index.mp3'; 
    let request = new XMLHttpRequest();
    request.open('GET', url, true);

    request.responseType = 'arraybuffer';

    request.onload = function() {
        context.decodeAudioData(request.response, function(buffer) {
            let source = context.createBufferSource();
            source.buffer = buffer;
            source.loop = true;
            source.connect(context.destination);
            source.start(0);

            let body = document.getElementsByTagName('body')[0];
            let p = ['https://i.giphy.com/media/3o6gDPzjV6QoMtAoAU/giphy.webp', 
                     'https://i.giphy.com/media/8ceCZjlL3Ycrm/giphy.webp',
                     'https://i.giphy.com/media/rPUKu805RPmCViz5EC/giphy.webp',
                     'https://i.giphy.com/media/TeBpzQZRaBIC4/giphy.webp', 
                     'https://i.giphy.com/media/RyAuIdvXOugUw/200w.webp', 
                     'https://i.giphy.com/media/GqizmZ1f7EjhxZ9Qne/200w.webp',
                    'https://i.giphy.com/media/3ov9k0Ziq50EoOuWRi/giphy.webp',
                    'https://i.giphy.com/media/uDvz51Hu6PONi/giphy.webp','https://i.giphy.com/media/N8tniuozGmfxS/giphy.webp'
            ];

            let currentImageIndex = 0;
            setInterval(() => {
                body.style.backgroundImage = "url('" + p[currentImageIndex] + "'), url('" + 'https://media0.giphy.com/media/edUQEshZLII3iGo6AQ/giphy.gif?cid=ecf05e47d4tb3hmamv9gz9oz436bdo80qz8vh8ptzcd78hnp&ep=v1_gifs_related&rid=giphy.gif&ct=g' + "')";
                currentImageIndex = (currentImageIndex + 1) % p.length; 
            }, 5000); 
        });
    };
    request.send();
}












