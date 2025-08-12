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
            case 'equals':
                let result
                if(previousInput && operator && currentInput){
                    result= calculate(parseFloat(previousInput), parseFloat(currentInput), operator)
                }
                updateDisplay(result.toString())
                currentInput=result.toString()
                previousInput=''
                operator=null
            case 'divide':
            case 'multiply':
            case 'additon':
            case 'subtract':
                if(currentInput){
                    if(previousInput && operator){
                        result= calculate(parseFloat(previousInput), parseFloat(currentInput), operator)
                    }
                    else{
                        previousInput= currentInput
                    }
                    currentInput=''
                    operator= getOperator(id)
                }
            
            default:
                console.log('shdjf')
        }
    })
})

function getOperator(id){
    switch(id){
        case 'divide':
            return '/'
        case 'multiply':
            return '*'
        case 'addition':
            return '+'
        case 'subtract':
            return '-'
    }
}
function calculate(a,b,op){
    switch(op){
        case '+':
            return a+b
        case '-':
            return a-b
        case '*':
            return a*b
        case '/':
            return a/b
    }
}

updateDisplay('')