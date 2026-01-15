const getCurrentYear = () => new Date().getFullYear();

export class Worker {
    /** Фамилия и инициалы */
    #fullName: string;

    get fullName() {
        return this.#fullName;
    }

    set fullName(fullName: string) {
        this.#fullName = fullName;
    }

    /** Название должности */
    #position: string;

    get position() {
        return this.#position;
    }

    set position(newPosition: string) {
        this.#position = newPosition;
    }

    /** Зарплата */
    #salary: number;

    get salary() {
        return this.#salary;
    }

    set salary(newSalary: number) {
        this.#salary = newSalary;
    }

    /** Год начала работы */
    #yearJoined: number;

    get yearJoined() {
        return this.#yearJoined;
    }

    set yearJoined(newYearJoined: number) {
        this.#yearJoined = newYearJoined;
    }

    /** Расчет стажа на текущий */
    get experience(): number {
        return getCurrentYear() - this.#yearJoined;
    }

    constructor();
    constructor(fullName: string, position: string, salary: number, yearJoined: number);
    constructor(fullName?: string, position?: string, salary?: number, yearJoined?: number) {
        this.#fullName = fullName ?? 'Неизвестно';
        this.#position = position ?? 'Стажер';
        this.#salary = salary ?? 0;
        this.#yearJoined = yearJoined ?? getCurrentYear();
    }

    displayInfo(): void {
        console.log(
            `Сотрудник: ${this.#fullName} | ` +
            `Должность: ${this.#position} | ` +
            `Зарплата: ${this.#salary} | ` +
            `Год начала: ${this.#yearJoined}`
        );
    }

    /** "Деструктор" (имитация для логики удаления из системы СБИС) */
    destroy(): void {
        console.log(`[Система] Запись о сотруднике ${this.#fullName} архивирована.`);
    }
}
