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

    function create_map(id, options) {
        let cord = [23.7696, 90.3576]
        if (options.cord) {
            cord = options.cord
        }

        return L.map(id, {
            center: cord,
            zoom: 17,
            zoomControl: false,
            dragging: true,
            maxZoom: 19,
            minZoom: 17
        });
    }

    function addMap(id, options, callBack) {

    }


    $(document).ready(function () {
        $(".toast").toast('show');
    });
})()

