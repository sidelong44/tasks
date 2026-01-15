import readline from 'readline';
import { Worker } from './Worker';

async function main() {
    const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

    const question = (str: string) => new Promise<string>((resolve, reject) => {
        try {
            rl.question(str, (result) => resolve(result));
        } catch (error) {
            reject(error);
        }
    });

    const workersList: Worker[] = [];

    console.log(`--- Корпоративная система управления персоналом ТЕНЗОР (${new Date().getFullYear()}) ---`);

    const count = parseInt(await question('Введите количество новых сотрудников для ввода: '));

    for (let i = 0; i < count; i++) {
        console.log(`\nВвод данных сотрудника #${i + 1}:`);
        const name = await question('Фамилия и инициалы: ');
        const pos = await question('Должность: ');
        const sal = parseFloat(await question('Зарплата (руб): '));
        const year = parseInt(await question('Год начала работы: '));

        const employee = new Worker(name, pos, sal, year);
        workersList.push(employee);
    }

    console.log('\n--- Фильтрация по стажу ---');
    const threshold = parseInt(await question('Введите минимальный стаж для поиска (в годах): '));

    const experiencedWorkers = workersList.filter(w => w.experience > threshold);

    if (experiencedWorkers.length > 0) {
        console.log(`\nСотрудники со стажем более ${threshold} лет:`);
        experiencedWorkers.forEach(w => {
            console.log(`- ${w.fullName} (Стаж: ${w.experience} лет)`);
        });
    } else {
        console.log(`\nВ компании «Тензор» нет сотрудников со стажем работы более ${threshold} лет.`);
    }

    // Демонстрация работы с объектом
    if (workersList.length > 0) {
        console.log('\n[Тест] Очистка первой записи...');
        workersList[0].destroy();
    }
}

main();
