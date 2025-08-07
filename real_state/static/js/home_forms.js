


// Reliza una comprobacion en el formulario antes de enviar para no hacer consultas vacias.

document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("filterform");
    let send = false;

    form.addEventListener("submit", function (event) {
        if (send) {
            event.preventDefault();
            console.log("El formulario ya fue enviado.");
            return;
        }

        const selects = form.querySelectorAll("select");
        let someselected = false;

        selects.forEach(select => {
            const value = select.value.trim().toLowerCase();
            if (value && value !== "todo" && value !== "tipo de propiedad" && value !== "region" && value !== "habitaciones" && value !== "baños") {
                someselected = true;
            }
        });

        if (!someselected) {
            event.preventDefault();
            alert("Selecciona al menos un filtro antes de buscar.");
            return;
        }
        send = true;
    });
});