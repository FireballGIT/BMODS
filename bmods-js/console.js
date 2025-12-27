const fs = require("fs");
const path = require("path");

const Console = {
    console: [],
    consoleExists: false,

    getTimestamp() {
        const now = new Date();
        const m = String(now.getMonth() + 1).padStart(2, "0");
        const d = String(now.getDate()).padStart(2, "0");
        const y = now.getFullYear();
        const h = String(now.getHours()).padStart(2, "0");
        const min = String(now.getMinutes()).padStart(2, "0");
        return `${m}/${d}/${y} ${h}:${min}`;
    },

    new(objectType) {
        if (objectType === "console") {
            this.console = [];
            this.consoleExists = true;
            console.log(`[${this.getTimestamp()}] Console object created/reset.`);
        } else if (objectType === "log") {
            console.log(`[${this.getTimestamp()}] Log object type not yet implemented.`);
        } else {
            console.log(`[${this.getTimestamp()}] ERROR! Invalid object type.`);
        }
    },

    log(msg) {
        if (this.consoleExists) {
            const timestamped = `[${this.getTimestamp()}] ${msg}`;
            this.console.push(timestamped);
            console.log(`Logged: '${timestamped}'`);
        } else {
            console.log(`[${this.getTimestamp()}] ERROR! No existing console object.`);
        }
    },

    terminate(index) {
        if (this.consoleExists) {
            if (index >= 0 && index < this.console.length) {
                const removed = this.console.splice(index, 1)[0];
                this.log(`Terminated line ${index}: '${removed}'`);
            } else {
                this.log(`ERROR! Index ${index} is out of range.`);
            }
        } else {
            console.log(`[${this.getTimestamp()}] ERROR! No existing console object.`);
        }
    },

    clear() {
        if (this.consoleExists) {
            this.console = [];
            this.log("Console cleared.");
        } else {
            console.log(`[${this.getTimestamp()}] ERROR! No existing console object.`);
        }
    },

    println(index) {
        if (this.consoleExists) {
            if (index >= 0 && index < this.console.length) {
                console.log(this.console[index]);
            } else {
                console.log(`[${this.getTimestamp()}] ERROR! Index ${index} is out of range.`);
            }
        } else {
            console.log(`[${this.getTimestamp()}] ERROR! No existing console object.`);
        }
    },

    prntall() {
        if (this.consoleExists) {
            if (this.console.length === 0) {
                this.log("Console is empty.");
                return;
            }
            console.log("--- Console Start ---");
            this.console.forEach(line => console.log(line));
            console.log("--- Console End ---");
        } else {
            console.log(`[${this.getTimestamp()}] ERROR! No existing console object.`);
        }
    },

    exportLog(filename = "output_log", directory = ".") {
        if (this.consoleExists && this.console.length > 0) {
            const dirPath = path.resolve(directory);
            if (!fs.existsSync(dirPath)) fs.mkdirSync(dirPath, { recursive: true });
            const filePath = path.join(dirPath, `${filename}.bmlog`);
            try {
                fs.writeFileSync(filePath, this.console.join("\n"), "utf8");
                this.log(`Successfully exported console to '${filePath}'.`);
            } catch (e) {
                this.log(`ERROR! Could not write to file ${filePath}: ${e}`);
            }
        } else if (this.consoleExists) {
            this.log("Console is empty; nothing to export.");
        } else {
            this.log("ERROR! No existing console object to export.");
        }
    }
};

module.exports = Console;
