let maps = new Map();

function create_map(id, options) {
    let center = [23.7696, 90.3576]
    let zoom = 17;
    let maxZoom = 19;
    let minZoom = 15;

    if (options) {
        center = options.center ? options.center : center;
        zoom = options.zoom ? options.zoom : zoom;
        maxZoom = options.maxZoom ? options.maxZoom : maxZoom;
        minZoom = options.minZoom ? options.minZoom : minZoom;
    }

    let map = L.map(id, {
        center: center,
        zoom: zoom,
        zoomControl: false,
        dragging: true,
        maxZoom: maxZoom,
        minZoom: minZoom
    });

    L.tileLayer('https://retina-tiles.p.rapidapi.com/local/osm{r}/v1/{z}/{x}/{y}.png?rapidapi-key=28d6cbb4b4msh167530a085cbcacp15d417jsn37ae52308258', {
        attribution: 'Tiles &copy: <a href="https://www.maptilesapi.com/retina-tiles/">Retina Tiles API</a>, Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        maxZoom: 19
    }).addTo(map);


    return map;
}

function addSearch(map) {
    const provider = new window.GeoSearch.OpenStreetMapProvider();

    const search = new GeoSearch.GeoSearchControl({
        provider: provider,
        style: 'button',
        showMarker: true,
        showPopup: true,
        marker: new L.marker({draggable: true, autoPan: false}),
        updateMap: true,
        autoClose: false
    });
    map.addControl(search)
}

function location_update(e) {
    let domId = e.sourceTarget._container.id;
    let callBack = maps.get(domId).callBack;
    callBack(e.location);
}

function addMap(id, options, callBack) {
    if (maps.has(id)) {
        return maps.get(id);
    }

    let map = create_map(id, options);
    maps.set(id, {
        map: map,
        options: options,
        callBack: callBack
    });

    if (options && options.showSearch) {
        addSearch(map);
        map.on('geosearch/showlocation', location_update);
    }

    map.on('click', function (e) {
        console.log(e)
    })

    setTimeout(function () {
        map.invalidateSize(true);
    }, 5000);

    return map;
}

function updateIputField(name, value) {
    $("input[name=" + name + "]").val(value);
}

function createModal(modalId){
    let myModal = new bootstrap.Modal(document.getElementById(modalId), {
            keyboard: false
        });
    return myModal;
}

function getElementOfModal(modalId){
    return document.getElementById(modalId);
}

(() => {
    'use strict'
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation');

    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            console.log('here..')
            if (!form.checkValidity()) {
                event.preventDefault()
                event.stopPropagation()
            }

            form.classList.add('was-validated')
        }, false)
    })

    let tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    })


    let toastElList = [].slice.call(document.querySelectorAll('.toast'))
    toastElList.map(function (toastEl) {
        return new bootstrap.Toast(toastEl, 'autohide')
    })

    $(document).ready(function () {
        $(".toast").toast('show');
    });
})()

