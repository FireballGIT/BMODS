const readlineSync = require("readline-sync");

const Tasker = {
    tasks: [],

    addTasks(numItems) {
        for (let i = 1; i <= numItems; i++) {
            const item = readlineSync.question(`${i}. Enter a task: `);
            this.tasks.push(item);
        }
    },

    showItem(index) {
        if (index >= 0 && index < this.tasks.length) {
            console.log(this.tasks[index]);
        } else {
            console.log(`Error: Index ${index} is out of range.`);
        }
    },

    removeItem(index) {
        if (index >= 0 && index < this.tasks.length) {
            const removed = this.tasks.splice(index, 1)[0];
            console.log(`Removed item: '${removed}'`);
        } else {
            console.log(`Error: Index ${index} is out of range. No item removed.`);
        }
    },

    showAll() {
        if (this.tasks.length === 0) {
            console.log("The task list is currently empty.");
        } else {
            console.log("Current Tasks:");
            this.tasks.forEach((item, idx) => console.log(`${idx + 1}. ${item}`));
        }
    },

    clear() {
        this.tasks = [];
    }
};

module.exports = Tasker;
