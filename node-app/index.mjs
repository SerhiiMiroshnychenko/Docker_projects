import fs from 'fs'

fs.appendFile('my-file.txt', 'Файл створено Node.js', (err) => {
    if (err) throw err
    console.log('Файл створено!')
})

setTimeout(() => console.log('Кінец'), 99000000)
