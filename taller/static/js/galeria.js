function obtenerImagenesDeAutos() {
    // Define la clave de API
    const apiKey = '8J8PWxWDsdWpMcAcwoJNWSoDet6wxBd2f2pSB900reX1rxebauog3NjK';
  
    // Realiza una solicitud de búsqueda a la API de Pexels
    fetch('https://api.pexels.com/v1/search?query=car', {
      headers: {
        Authorization: apiKey,
      },
    })
      .then(response => response.json())
      .then(data => {
        // Obtiene la lista de imágenes de autos
        const photos = data.photos;
  
        // Muestra las imágenes en la página HTML
        const galleryContainer = document.getElementById('gallery');
  
        photos.forEach(photo => {
          const imgElement = document.createElement('img');
          imgElement.src = photo.src.original;
          imgElement.alt = 'Car';
          galleryContainer.appendChild(imgElement);
        });
      })
      .catch(error => {
        console.log('Error:', error);
      });
  }