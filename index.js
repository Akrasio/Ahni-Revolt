const { Client } = require("revolt.js");
const { Collection } = require('discord.js');
const cron = require("node-cron");
require("dotenv").config();
const { setStatus, onCoolDown, renameChannel, setTimeStatus, log, evalCmd, Style, AhniEndPoints, AhniRegExp } = require("./functions");
let client = new Client();
client.cooldowns = new Collection();
const { AhniClient } = require("ahnidev");
const Ahni = new AhniClient({ KEY: process.env.AHNIKEY, url: "https://ahni.dev" });

client.once("ready", async () => {
    log(Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
    log(Style.bg.blue, `Logged in as ${client.user.username}! | ${client.servers.size} Servers!`);
    if (!process.env.TimeChannel) return;
    renameChannel(client, { channelId: process.env["TimeChannel"] });
});

cron.schedule("* * * * *", () => {
    setTimeStatus(client);
    if (!process.env.TimeChannel) return;
    renameChannel(client, { channelId: process.env["TimeChannel"] });
})
client.on("message", async (message) => {
    if (message.author.bot || message.system || !message.content) return;
    const args = message.content.slice(process.env.PREFIX.length).trim().split(/ +/);
    const commandName = args.shift().toLowerCase();
    if (!message.content.startsWith(process.env.PREFIX)) return;
    if (onCoolDown(message, commandName)) {
        const cool = { colour: "#FF0000", description: `❌ Please wait ${require("ms")(Math.round(onCoolDown(message, commandName) * 1000))} before reusing the \`${commandName}\` command` }
        return message.channel.sendMessage({ content: " ", embeds: [cool] }).then(msg => {
            setTimeout(() => {
                msg.delete().catch(err => {
                    log(Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
                    log(Style.bg.red, "User: " + message.author.username + ` [${message.author_id}] ` + " | Command: " + commandName + " | Args: " + (args?.join(" ") || "NONE"))
                    log(Style.fg.red, err.message);
                });
            }, 4000)
        });
    }
    if (commandName == "eval") {
        if (message.author_id !== process.env.OWNERID) return;
        const code = args.join(" ");
        return evalCmd(message, code);
    };
    if (commandName === "ping") {
        await message.channel.sendMessage("pong. :ping_pong:").catch(err => {
            log(Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
            log(Style.bg.red, "User: " + message.author.username + ` [${message.author_id}] ` + " | Command: " + commandName + " | Args: " + (args?.join(" ") || "NONE"))
            log(Style.fg.red, err.message);
            return;
        });

        log(Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
        return log(Style.fg.green, "User: " + message.author.username + ` [${message.author_id}] ` + " | Command: " + commandName + " | Args: " + (args?.join(" ") || "NONE"))
    };
    if (commandName === "help") {
        const embedHelp = { title: client.user.username + " | commands", colour: "#AEFAEF", description: `| Name | Description|\n| - | - |\n| help | Sends the commands list! |\n| nsfw | Sends requested NSFW image from Ahni.dev API |\n| ping | Pong? |\n| contact | Send a message to the developers about a bug or image issue |` }
        await message.channel.sendMessage({ content: " ", embeds: [embedHelp] }).catch(err => {
            log(Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
            log(Style.bg.red, "User: " + message.author.username + ` [${message.author_id}] ` + " | Command: " + commandName + " | Args: " + (args?.join(" ") || "NONE"))
            log(Style.fg.red, err.message);
            return;
        });
        log(Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
        return log(Style.fg.green, "User: " + message.author.username + ` [${message.author_id}] ` + " | Command: " + commandName + " | Args: " + (args?.join(" ") || "NONE"))

    }
    if (commandName == "nsfw") {
        log(Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
        log(Style.fg.green, "User: " + message.author.username + ` [${message.author_id}] ` + " | Command: " + commandName + " | Args: " + (args?.join(" ") || "NONE"));
        if (!message.channel.nsfw) return message.channel.sendMessage("This channel is __not__ an NSFW marked channel!");
        const embed = { colour: "#FF0000", description: `Please provide one of the following args:\n \`${AhniEndPoints.join("\`, \`")}\`` }
        if (args.length < 1) return message.channel.sendMessage({ content: " ", embeds: [embed] });
        const matched = args[0].match(AhniRegExp)
        if (!matched) return message.channel.sendMessage({ content: " ", embeds: [embed] });
        await Ahni.nsfw(matched).then(async res => {
            return message.channel.sendMessage({ content: `[ ](${res.result})\n> $\\widetilde{Here \\space is \\space your \\space ${matched} \\space image}$` }).catch(err => {
                log(Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
                log(Style.bg.red, "User: " + message.author.username + ` [${message.author_id}] ` + " | Command: " + commandName + " | Args: " + (args?.join(" ") || "NONE"))
                log(Style.fg.red, err.message);
                return;
            });
        })
    };
    if (commandName == "contact") {
        if (args.length < 5) message.reply("Please describe your issue in more than 5 Words!")
        log(Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
        log(Style.fg.green, "User: " + message.author.username + ` [${message.author_id}] ` + " | Command: " + commandName + " | Args: " + (args?.join(" ") || "NONE"))
        return client.channels.get(process.env.REPORTS).sendMessage(`New Contact:\n User: ${message.author.username}\n[${message.author_id}]\n\n> Message: ${args.join(" ")}`).catch(err => {
            log(Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
            log(Style.bg.red, "User: " + message.author.username + ` [${message.author_id}] ` + " | Command: " + commandName + " | Args: " + (args?.join(" ") || "NONE"))
            log(Style.fg.red, err.message);
            return;
        });
    }
    if (commandName == "mask") {
        if (message.author_id !== process.env.OWNERID) return;
        const name = message.author.username;
        const avatar = message.author.avatar;
        log(Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
        log(Style.fg.green, "User: " + message.author.username + ` [${message.author_id}] ` + " | Command: " + commandName + " | Args: " + (args?.join(" ") || "NONE"));
        return message.channel.sendMessage({
            content: args.join(" ").replace(/\<\@/g, "<@ "), masquerade: {
                name: `${message.author.username}`,
                avatar: `${message.author.generateAvatarURL({ size: 512 })}`,
            }
        }).catch(err => {
            log(Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
            log(Style.bg.red, "User: " + message.author.username + ` [${message.author_id}] ` + " | Command: " + commandName + " | Args: " + (args?.join(" ") || "NONE"))
            log(Style.fg.red, err.message);
            return;
        });
    }
});

process.on("unhandledRejection", (err) => log(Style.fg.red, `${err.message}`));
process.on("uncaughtException", (err) => log(Style.fg.green, `${err.message}`));
process.on("warning", (err) => log(Style.fg.yellow, `${err.message}`));
client.loginBot(process.env.BOT_TOKEN);