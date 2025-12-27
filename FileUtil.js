const fs = require('fs');
const path = require('path');
const AdmZip = require('adm-zip');

const FileUtil = {
    make(filePath, content = "") {
        if (fs.existsSync(filePath)) return "Error: File already exists.";
        fs.writeFileSync(filePath, content, 'utf8');
        return true;
    },

    rename(oldPath, newName) {
        if (!fs.existsSync(oldPath)) return "Error: Path does not exist.";
        const newPath = path.join(path.dirname(oldPath), newName);
        fs.renameSync(oldPath, newPath);
        return newPath;
    },

    renameExt(filePath, newExt) {
        if (!fs.existsSync(filePath) || !fs.lstatSync(filePath).isFile()) return "Error: File does not exist.";
        if (!newExt.startsWith('.')) newExt = '.' + newExt;
        const base = path.join(path.dirname(filePath), path.basename(filePath, path.extname(filePath)));
        const newPath = base + newExt;
        fs.renameSync(filePath, newPath);
        return newPath;
    },

    move(src, dst) {
        if (!fs.existsSync(src)) return "Error: Source does not exist.";
        fs.renameSync(src, dst);
        return true;
    },

    compress(folderPath, outputZip) {
        if (!fs.existsSync(folderPath) || !fs.lstatSync(folderPath).isDirectory()) return "Error: Folder does not exist.";
        if (!outputZip.endsWith('.zip')) outputZip += '.zip';
        const zip = new AdmZip();
        zip.addLocalFolder(folderPath);
        zip.writeZip(outputZip);
        return outputZip;
    },

    extract(zipPath, outputDir) {
        if (!fs.existsSync(zipPath)) return "Error: Not a valid ZIP file.";
        const zip = new AdmZip(zipPath);
        zip.extractAllTo(outputDir, true);
        return true;
    }
};

module.exports = FileUtil;
