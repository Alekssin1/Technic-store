const rangeSlider = document.getElementById("range__slider");

if (rangeSlider) {
    noUiSlider.create(rangeSlider, {
        start: [0, 120000],
        connect: true,
        step: 1,
        range: {
            'min': 0,
            'max': 120000
        }
    });

    const inputStart = document.getElementById("price__start");
    const inputEnd = document.getElementById("price__end");

    const inputs = [inputStart, inputEnd];

    rangeSlider.noUiSlider.on('update', function (values, handle) {
        inputs[handle].value = Math.round(values[handle]);
    });

    const setRangeSlider = (i, value) => {
        let arr = [null, null];
        arr[i] = value;


        rangeSlider.noUiSlider.set(arr);
    }

    inputs.forEach((el, index) => {
        el.addEventListener('change', (e) => {
            setRangeSlider(index, e.currentTarget.value)
        });
    });
}