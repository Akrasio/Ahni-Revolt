const { Collection } = require('discord.js');
const axios = require("axios");
require("dotenv").config();
const util = require("util");

module.exports.AhniEndPoints = AhniEndPoints = ["ass", "assgif", "athighs", "bbw", "bdsm", "blow", "boobs", "feet", "furfuta", "furgif", "futa", "gifs", "hboobs", "hentai", "hfeet", "neko", "irlfemb", "jackopose", "milk", "pantsu", "sex", "slime", "thighs", "trap", "yuri", "latex"];
module.exports.AhniRegExp = AhniRegExp = new RegExp(`assgif|ass|athighs|bbw|bdsm|blow|boobs|feet|furfuta|furgif|futa|gifs|hboobs|hentai|hfeet|neko|irlfemb|jackopose|milk|pantsu|sex|slime|thighs|trap|yuri|latex`, "i");
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
    return client.channels.get(channelId).edit({ name: `${month}/${date}, ${hours <= 9 ? "0" + hours : hours}:${minutes <= 9 ? "0" + minutes : minutes} EST` }).catch(err => {
        log(this.Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
        log(this.Style.fg.red, err.message);
        return;
    });
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
    return setStatus(client, { text: `${hours <= 9 ? "0" + hours : hours}:${minutes <= 9 ? "0" + minutes : minutes}` + " EST | =help", presence: state })
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
        let evaled = eval(code);
        const TOKEN = new RegExp(`${process.env.BOT_TOKEN}`, "gi");
        const OWNERID = new RegExp(`${process.env.OWNERID}`, "gi");
        if (typeof evaled !== "string") evaled = await util.inspect(evaled);
        const embeded = { icon_url: message.author.generateAvatarURL({ size: 512 }), title: message.author.username + " | Eval", description: `${evaled.replace(TOKEN, "N0Tt0DaYB0ZoxD")}`, colour: "#33ff00" }
        message.channel.sendMessage({ content: " ", embeds: [embeded] });
    } catch (err) {
        message.channel.sendMessage(`\`ERROR\` \`\`\`xl\n${(err)}\n\`\`\``);
    }
}

const log = (color, text) => {
    console.log(`${color}%s${this.Style.reset}`, text);
};

module.exports.log = log;
module.exports.evalCmd = evalCmd;
module.exports.setStatus = setStatus;
module.exports.onCoolDown = onCoolDown;
module.exports.renameChannel = renameChannel;
module.exports.setTimeStatus = setTimeStatus;