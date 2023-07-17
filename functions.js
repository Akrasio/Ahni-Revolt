const { Collection } = require('discord.js');
const axios = require("axios");
require("dotenv").config();
const util = require("util");
module.exports.AhniEndPoints = AhniEndPoints = ["ass", "assgif", "athighs", "bbw", "bdsm", "blow", "boobs", "feet", "furfuta", "furgif", "futa", "gifs", "hass", "hboobs", "hentai", "hfeet", "neko", "irlfemb", "jackopose", "milk", "pantsu", "sex", "slime", "thighs", "femboy", "yuri","tentacle", "latex"];
module.exports.AhniRegExp = AhniRegExp = new RegExp(`assgif|ass|athighs|bbw|bdsm|blow|boobs|feet|furfuta|furgif|futa|gifs|hass|hboobs|hentai|hfeet|neko|irlfemb|jackopose|milk|pantsu|sex|slime|thighs|femboy|tentacle|yuri|latex`, "i");
module.exports.AhniActEndPoints = AhniActEndPoints = ["boop","bonk","kiss","hug"];
module.exports.AhniActRegExp = AhniActRegExp = new RegExp(`boop|bonk|kiss|hug`, "i");
module.exports.Style = Style = {
    reset: "\x1b[0m",
    bright: "\x1b[1m",
    dim: "\x1b[2m",
    underscore: "\x1b[4m",
    blink: "\x1b[5m",
    reverse: "\x1b[7m",
    hidden: "\x1b[8m",
    fg: {
        black: "\x1b[30m",
        red: "\x1b[31m",
        green: "\x1b[32m",
        yellow: "\x1b[33m",
        blue: "\x1b[34m",
        magenta: "\x1b[35m",
        cyan: "\x1b[36m",
        white: "\x1b[37m",
        crimson: "\x1b[38m"
    },
    bg: {
        black: "\x1b[40m",
        red: "\x1b[41m",
        green: "\x1b[42m",
        yellow: "\x1b[43m",
        blue: "\x1b[44m",
        magenta: "\x1b[45m",
        cyan: "\x1b[46m",
        white: "\x1b[47m",
        crimson: "\x1b[48m"
    }

};

async function setStatus(client, { text: text, presence: presence }) {
    await axios.patch(
        `${client.apiURL}/users/@me`,
        {
            status: { text, presence }
        },
        {
            headers: {
                'x-bot-token': process.env['BOT_TOKEN']
            }
        }
    );
};

async function renameChannel(client, { channelId: channelId }) {
    let date_ob = new Date();
    let date = ("0" + date_ob.getDate()).slice(-2);
    let month = ("0" + (date_ob.getMonth() + 1)).slice(-2);
    let year = date_ob.getFullYear();
    let hours = date_ob.getHours();
    let minutes = date_ob.getMinutes();
    let seconds = date_ob.getSeconds();
    const channel = await client.channels.get(channelId);
    if (channel) {
        channel.edit({ name: `${month}/${date}, ${hours <= 9 ? "0" + hours : hours}:${minutes <= 9 ? "0" + minutes : minutes} EST` }).catch(err => {
            log(this.Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
            log(this.Style.fg.red, err.message);
            return;
        })
    } else {
        return log(this.Style.fg.red, `Channel with ID ${channelId} was NOT found`)
    }
};
async function setTimeStatus(client) {
    let date_ob = new Date();
    let date = ("0" + date_ob.getDate()).slice(-2);
    let month = ("0" + (date_ob.getMonth() + 1)).slice(-2);
    let year = date_ob.getFullYear();
    let hours = date_ob.getHours();
    let minutes = date_ob.getMinutes();
    let seconds = date_ob.getSeconds();
    let state = "";
    if (0 <= hours && hours <= 5) state = "Busy";
    if (6 <= hours && hours <= 12) state = "Idle";
    if (13 <= hours && hours <= 21) state = "Online";
    if (22 <= hours && hours <= 23) state = "Busy";
    return await setStatus(client, { text: `${hours <= 9 ? "0" + hours : hours}:${minutes <= 9 ? "0" + minutes : minutes}` + `EST | ${process.env.PREFIX}help`, presence: state })
};

function onCoolDown(message, command) {
    if (!message || !message.client) throw "No Message with a valid Revolt Client granted as First Parameter";
    if (!command || !command) throw "No Command with a valid Name granted as Second Parameter";
    const client = message.client;
    if (!client.cooldowns.has(command)) { //if its not in the cooldown, set it too there
        client.cooldowns.set(command, new Collection());
    }
    const now = Date.now(); //get the current time
    const timestamps = client.cooldowns.get(command); //get the timestamp of the last used commands
    const cooldownAmount = 4 * 1000; //get the cooldownamount of the command, if there is no cooldown there will be automatically 1 sec cooldown, so you cannot spam it^^
    if (timestamps.has(message.author_id)) { //if the user is on cooldown
        const expirationTime = timestamps.get(message.author_id) + cooldownAmount; //get the amount of time he needs to wait until he can run the cmd again
        if (now < expirationTime) { //if he is still on cooldonw
            const timeLeft = (expirationTime - now) / 1000; //get the lefttime
            return timeLeft
        }
        else {
            //if he is not on cooldown, set it to the cooldown
            timestamps.set(message.author_id, now);
            //set a timeout function with the cooldown, so it gets deleted later on again
            setTimeout(() => timestamps.delete(message.author_id), cooldownAmount);
            //return false aka not on cooldown
            return false;
        }
    }
    else {
        //if he is not on cooldown, set it to the cooldown
        timestamps.set(message.author_id, now);
        //set a timeout function with the cooldown, so it gets deleted later on again
        setTimeout(() => timestamps.delete(message.author_id), cooldownAmount);
        //return false aka not on cooldown
        return false;
    }
};

async function evalCmd(message, code) {
    try {
	let client = message.client;
        let evaled = eval(code);
        const TOKEN = new RegExp(`${process.env.BOT_TOKEN}`, "gi");
        const OWNERID = new RegExp(`${process.env.OWNERID}`, "gi");
        if (typeof evaled !== "string") evaled = await util.inspect(evaled);
        const embeded = { icon_url: message.author.generateAvatarURL({ size: 512 }), title: message.author.username + " | Eval", description: `${evaled.replace(TOKEN, "N0Tt0DaYB0ZoxD")}`, colour: "#33ff00" }
        message.channel.sendMessage({ content: " ", embeds: [embeded] }).then(async msg =>{
		await message.delay(5000);
		return msg.delete();
	})
    } catch (err) {
        message.channel.sendMessage(`__ERROR__:\n\n\`\`\`xl\n${(err)}\n\`\`\``).then(async msg=>{
	await message.delay(4000)
		msg.delete()
	})
    }
}

const log = (color, text) => {
    console.log(`${color}%s${this.Style.reset}`, text);
};

"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function () { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function () { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (_) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.UploadFile = void 0;
var axios_1 = require("axios");
var boundary = "------REJECTJS";
function appendFormData(name, data, fileName) {
    var fileBuffer = [];
    if (!data)
        return;
    var str = "\r\n--".concat(boundary, "\r\nContent-Disposition: form-data; name=\"").concat(name, "\"; filename=\"").concat(fileName, "\"");
    if (data instanceof Buffer) {
        str += "\r\nContent-Type: application/octet-stream";
    }
    else if (data instanceof Object) {
        str += "\r\nContent-Type: application/json";
        // eslint-disable-next-line no-param-reassign
        data = Buffer.from(JSON.stringify(data));
    }
    else {
        // eslint-disable-next-line no-param-reassign
        data = Buffer.from("".concat(data));
    }
    fileBuffer.push(Buffer.from("".concat(str, "\r\n\r\n")));
    fileBuffer.push(data);
    fileBuffer.push(Buffer.from("\r\n--".concat(boundary, "--")));
    return fileBuffer;
}
function UploadFile(file, type) {
    if (type === void 0) { type = "attachments"; }
    return __awaiter(this, void 0, void 0, function () {
        var data, response;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    data = Buffer.concat(appendFormData("file", file.file, file.name));
                    return [4 /*yield*/, axios_1.default.post("https://autumn.revolt.chat/".concat(type), data, {
                        headers: { "Content-Type": "multipart/form-data; boundary=".concat(boundary) },
                    })];
                case 1: return [4 /*yield*/, (_a.sent()).data];
                case 2:
                    response = (_a.sent());
                    return [2 /*return*/, response.id];
            }
        });
    });
}

async function createFileBuffer(url) {
    const res = Buffer.from(
        await (await axios.get(url, { responseType: "arraybuffer" })).data,
    );
    return res;
}
async function attach(url, fileName) {
    if (!fileName) return "No File Name Provided!"
   let fileUp = await UploadFile({
        name: fileName,
        file: await createFileBuffer(url)
    }).catch(() => undefined)
    return fileUp;
}
module.exports.createFileBuffer = createFileBuffer;
module.exports.UploadFile = UploadFile;
module.exports.log = log;
module.exports.attach = attach;
module.exports.evalCmd = evalCmd;
module.exports.setStatus = setStatus;
module.exports.onCoolDown = onCoolDown;
module.exports.renameChannel = renameChannel;
module.exports.setTimeStatus = setTimeStatus;
