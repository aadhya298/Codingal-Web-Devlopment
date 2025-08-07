const display = document.querySelector('.display')
const numberButtons = document.querySelectorAll('.number')
const operatorButtons = document.querySelectorAll('.operator')

let currentInput = ''
let previousInput = ''
let operator = null

function updateDisplay(value) {
    display.textContent = value || '0'
}

numberButtons.forEach(b => {
    b.addEventListener('click', () => {
        currentInput = currentInput + b.id
        updateDisplay(currentInput)
    })
})

operatorButtons.forEach(b => {
    b.addEventListener('click', () => {
        const id = b.id
    switch (id) {
            case 'clear':
                currentInput = ''
                previousInput = ''
                operator = null
                updateDisplay('')
                break
            case 'backspace':
               currentInput = currentInput.slice(0, -1)
                updateDisplay(currentInput)
                break;
            default:
                console.log('shdjf')
        }
    })
})
// 124*923493