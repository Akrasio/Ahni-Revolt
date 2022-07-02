const { Client } = require("revolt.js");
const { Collection } = require('discord.js');
const cron = require("node-cron");
const fs = require('fs');
require("dotenv").config();
const { attach, setStatus, createFileBuffer, onCoolDown, renameChannel, setTimeStatus, UploadFile, log, evalCmd, Style, AhniEndPoints, AhniRegExp, TestRegExp } = require("./functions");
let client = new Client();
client.cooldowns = new Collection();
const { AhniClient } = require("ahnidev");
const Ahni = new AhniClient({ KEY: process.env.AHNIKEY, url: process.env.AhniURL || "https://ahni.dev" });
const { RandomPHUB } = require('discord-phub');
const nsfw = new RandomPHUB(unique = false);

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
    if (!message.content.startsWith(process.env.PREFIX)) return;

    const args = message.content.slice(process.env.PREFIX.length).trim().split(/ +/);
    const commandName = args.shift().toLowerCase();
    if (!commandName) return;
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
    if (commandName === "av" || commandName == "avatar") {
        const targetName = (message.mentions?.length >= 1 ? message.mentions[0]?.username : message.author.username)
        const target = message.mentions?.length >= 1 ? message.mentions[0]?.generateAvatarURL({ size: 4096 }, true) ? message.mentions[0]?.generateAvatarURL({ size: 4096 }, true) : message.mentions[0]?.defaultAvatarURL : message.member.generateAvatarURL({ size: 4096 }, true) ? message.member.generateAvatarURL({ size: 4096 }, true) : message.member.generateAvatarURL({ size: 4096 }, true) ? message.author.generateAvatarURL({ size: 4096 }, true) : message.author.generateAvatarURL({ size: 4096 }, true) ? message.author.generateAvatarURL({ size: 4096 }, true) : message.member.user.defaultAvatarURL
        const embed = { description: "Avatar for [" + targetName + "](" + target + ")", colour: "#00FFFF", iconURL: target }

        await message.channel.sendMessage({ content: "[ ](" + target + ")", embeds: [embed] }).catch(err => {
            log(Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
            log(Style.bg.red, "User: " + message.author.username + ` [${message.author_id}] ` + " | Command: " + commandName + " | Args: " + (args?.join(" ") || "NONE"))
            log(Style.fg.red, err.message);
            return;
        });

        log(Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
        return log(Style.fg.green, "User: " + message.author.username + ` [${message.author_id}] ` + " | Command: " + commandName + " | Args: " + (args?.join(" ") || "NONE"))
    };
    if (commandName === "help") {
        const embedHelp = { title: client.user.username + " | commands", colour: "#AEFAEF", description: `| Name | Description|\n| - | - |\n| help | Sends the commands list! |\n| nsfw | Sends requested NSFW image from Ahni.dev API |\n| ping | Pong? |\n| contact | Send a message to the developers about a bug or image issue |\n| quote | Quote a message from this channel.|\n| avatar | Get a members Server or Global avatar.` }
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
        const embed = { colour: "#FF0000", description: `Please provide one of the following args:\n \`${TestEndPoints.join("\`, \`")}\`, \`${AhniEndPoints.join("\`, \`")}\`` }
        if (args.length < 1) return message.channel.sendMessage({ content: " ", embeds: [embed] });
        const matched = args[0].match(AhniRegExp)
        const matchedNew = args[0].match(TestRegExp)
        if (!matched && !matchedNew) return message.channel.sendMessage({ content: " ", embeds: [embed] });
        if (matched) return message.channel.sendMessage({ content: "One moment..." }).then(async (m) => {
            return await Ahni.nsfw(matched).then(async res => {
		const fileUp = await attach(process.env.AhniURL2 ? res.result.replace("https://ahni.dev", process.env.AhniURL2) : res.result, "NSFW")
                const embed = { media: fileUp, colour: "#00FFFF", description: `[Image URL](${res.result})` }
                return m.edit({ content: " ", embeds: [embed] }).catch(err => {
                    log(Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
                    log(Style.bg.red, "User: " + message.author.username + ` [${message.author_id}] ` + " | Command: " + commandName + " | Args: " + (args?.join(" ") || "NONE"))
                    log(Style.fg.red, err.message);
                })
            });
        })
            if (matchedNew) return message.channel.sendMessage({ content: "One moment..." }).then(async (m) => {
		console.log(nsfw.getRandomInCategory(matchedNew[0]).url)
		const fileUp = await attach(nsfw.getRandomInCategory(matchedNew[0]).url, "NSFW")
                const embed = { media: fileUp, colour: "#00FFFF", description: `[Image URL](${nsfw.getRandomInCategory(matched).url})` }
                return m.edit({ content: " ", embeds: [embed] }).catch(err => {
                    log(Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
                    log(Style.bg.red, "User: " + message.author.username + ` [${message.author_id}] ` + " | Command: " + commandName + " | Args: " + (args?.join(" ") || "NONE"))
                    log(Style.fg.red, err.message);
                })
            });
    };
    if (commandName.match(TestRegExp)) {
        log(Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
        log(Style.fg.green, "User: " + message.author.username + ` [${message.author_id}] ` + " | Command: " + commandName + " | Args: " + (args?.join(" ") || "NONE"));
        if (!message.channel.nsfw) return message.channel.sendMessage("This channel is __not__ an NSFW marked channel!");
        const matched = commandName.match(TestRegExp)[0]
	if (!matched) return message.channel.sendMessage({ content: " ", embeds: [embed] });
        return message.channel.sendMessage({ content: "One moment..." }).then(async (m) => {
		const fileUp = await attach(nsfw.getRandomInCategory(matched).url, "NSFW")
                const embed = { media: fileUp, colour: "#00FFFF", description: `[Image URL](${nsfw.getRandomInCategory(matched).url})` }
                m.edit({ content: " ", embeds: [embed] }).catch(err => {
                    log(Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
                    log(Style.bg.red, "User: " + message.author.username + ` [${message.author_id}] ` + " | Command: " + commandName + " | Args: " + (args?.join(" ") || "NONE"))
                    log(Style.fg.red, err.message);
                    return console.log(res)
                })
            });
    }

    if (commandName.match(AhniRegExp)) {
        log(Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
        log(Style.fg.green, "User: " + message.author.username + ` [${message.author_id}] ` + " | Command: " + commandName + " | Args: " + (args?.join(" ") || "NONE"));
        if (!message.channel.nsfw) return message.channel.sendMessage("This channel is __not__ an NSFW marked channel!");
        const matched = commandName.match(AhniRegExp)
        if (!matched) return message.channel.sendMessage({ content: " ", embeds: [embed] });
        return message.channel.sendMessage({ content: "One moment..." }).then(async (m) => {
            await Ahni.nsfw(matched).then(async res => {
		const fileUp = await attach(process.env.AhniURL2 ? res.result.replace("https://ahni.dev", process.env.AhniURL2) : res.result, "NSFW")
                const embed = { media: fileUp, colour: "#00FFFF", description: `[Image URL](${res.result})` }
                m.edit({ content: " ", embeds: [embed] }).catch(err => {
                    log(Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
                    log(Style.bg.red, "User: " + message.author.username + ` [${message.author_id}] ` + " | Command: " + commandName + " | Args: " + (args?.join(" ") || "NONE"))
                    log(Style.fg.red, err.message);
                    return console.log(res)
                })
            });
        })
    }
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
        log(Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
        log(Style.fg.green, "User: " + message.author.username + ` [${message.author_id}] ` + " | Command: " + commandName + " | Args: " + (args?.join(" ") || "NONE"));
        if (!message.channel.havePermission("Masquerade", "SendMessage")) {
            return log(Style.fg.blue, `I lack one of the needed perms: \`SendMessage\`, \`Masquerade\`, or \`SendEmbeds\``);
        }
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
    if (commandName == "quote") {
        if (!message.member.hasPermission("ManageMessages")) return message.reply("You need `Manage Messages` permission to use this command!");
        const name = message.author.username;
        const avatar = message.author.avatar;
        const content2 = await message.channel.fetchMessage(args[0])
        const content = await message.channel.fetchMessagesWithUsers(args[0])
        if (content2.channel.nsfw && !message.channel.nsfw) return message.reply("Nice try lol... that message was in an nsfw channel.")
        log(Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
        log(Style.fg.green, "User: " + message.author.username + ` [${message.author_id}] ` + " | Command: " + commandName + " | Args: " + (args?.join(" ") || "NONE"));
        return message.reply({
            content: content2.content || "No Content Found:", masquerade: {
                name: `${content2.author.username}`,
                avatar: `${content2.author.generateAvatarURL({ size: 512 })}`,
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
process.on("error", (err) => log(Style.fg.red, `${err.message}`));
client.loginBot(process.env.BOT_TOKEN);
