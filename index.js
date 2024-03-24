const { Client } = require("revolt.js");
const { Collection } = require('discord.js');
const cron = require("node-cron");
const fs = require('fs');
const delay = require("delay");
const Rev = require('revoltbots.js');
const Uploader = require("revolt-uploader");
require("dotenv").config();
const api = new Rev.Client(process.env.rblapi);
const { attach, createFileBuffer, setStatus, onCoolDown, renameChannel, setTimeStatus, UploadFile, log, evalCmd, Style, AhniActEndPoints, AhniActRegExp, AhniEndPoints, AhniRegExp} = require("./functions");
let client = new Client();
client.cooldowns = new Collection();
const { AhniClient } = require("ahnidev");
const Ahni = new AhniClient({ KEY: process.env.AHNIKEY, url: process.env.AhniURL || "https://kyra.tk" });
client.ahni = Ahni;
client.rbl = api;
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
client.on("member/join", async(member)=>{
	if (member._id.server !== process.env.supportId) return;
        await member.edit({roles: [process.env.joinRole]});
})

client.once("ready", async()=>{
	api.autopostStats(client.servers.size.toString()).then(result => {
    		console.log("RBL : "+result)
	});
})

client.on("message", async (message) => {
message.delay = delay;
    if (message.author.bot || message.system || !message.content) return;
    let prefix = process.env.PREFIX;
    if (message.content.startsWith(process.env.PREFIX)){
	prefix = process.env.PREFIX
    } else if (message.content.startsWith(process.env.PREFIX2)){
	prefix = process.env.PREFIX2
    }
    if (!message.content.toLowerCase().startsWith(prefix.toLowerCase())) return;
    const args = message.content.slice(prefix.length).trim().split(/ +/);
    const commandName = args.shift().toLowerCase();
    if (!commandName) return;
    if (!message.channel.havePermission("SendMessage")) return;
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
    if (commandName == "vote") {
        log(Style.fg.green, "User: " + message.author.username + ` [${message.author_id}] ` + " | Command: " + commandName + " | Args: " + (args?.join(" ") || "NONE"))
	return message.reply("Vote here on [Revolt Bot List](<https://revoltbots.org/bots/01FEYFMPWJSJZ0671REAQMP6TY/vote>)").catch(err=>{
            log(Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
            log(Style.fg.red, err.message);
		return;
	})
    }
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
        const embedHelp = { title: client.user.username + " | commands", colour: "#AEFAEF", description: `| Name | Description|\n| - | - |\n| help | Sends the commands list! |\n| nsfw | Sends requested NSFW image from Ahni.dev API |\n| ping | Pong? |\n| contact | Send a message to the developers about a bug or image issue |\n| quote | Quote a message from this channel.|\n| avatar | Get a members Server or Global avatar.|\n| action | Do a thing with or to another member. |\n| vote | Vote for me on the bot list! |` }
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
        const matched = args[0].toLowerCase().match(AhniRegExp)
        if (!matched) return message.channel.sendMessage({ content: " ", embeds: [embed] });
        if (matched) return message.channel.sendMessage({ content: "One moment..." }).then(async (m) => {
            return await Ahni.nsfw(matched).then(async res => {
		const a = "SPOILER_"+res.result.toString().split("/")[7]
		const fileUp = await attach(process.env.AhniURL2 ? res.result.replace("https://kyra.tk", process.env.AhniURL2) : res.result, a)
                const embed = { media: fileUp, colour: "#00FFFF"}//, description: `[Image URL](${res.result})` }
                return m.edit({ files: fileUp, content: " ", embeds: [embed] }).catch(err => {
                    log(Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
                    log(Style.bg.red, "User: " + message.author.username + ` [${message.author_id}] ` + " | Command: " + commandName + " | Args: " + (args?.join(" ") || "NONE"))
                    log(Style.fg.red, err.message);
                })
            });
        })
    };

    if (commandName == "action") {
        log(Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
        log(Style.fg.green, "User: " + message.author.username + ` [${message.author_id}] ` + " | Command: " + commandName + " | Args: " + (args?.join(" ") || "NONE"));
        const embed = { colour: "#FF0000", description: `Please provide one of the following args:\n \`${AhniActEndPoints.join("\`, \`")}\`` }
        if (args.length < 1) return message.channel.sendMessage({ content: " ", embeds: [embed] });
        const matched = args[0].toLowerCase().match(AhniActRegExp);
	if (message.mention_ids == null) return message.reply({content: "Please provide a member!"});
        if (!matched) return message.channel.sendMessage({ content: " ", embeds: [embed] });
        if (matched) return message.channel.sendMessage({ content: "One moment..." }).then(async (m) => {
            return await Ahni.others(matched).then(async res => {
		const a = "SPOILER_"+matched[0]+".gif";
		const fileUp = await attach(process.env.AhniURL2 ? res.result.replace("https://kyra.tk", process.env.AhniURL2) : res.result, a)
                const embed = { media: fileUp, colour: "#00FFFF", description: `<@${message.mention_ids[0]}> is ${matched}ed by <@${message.author_id}>` }
                return m.edit({ content: " ", embeds: [embed] }).catch(err => {
                    log(Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
                    log(Style.bg.red, "User: " + message.author.username + ` [${message.author_id}] ` + " | Command: " + commandName + " | Args: " + (args?.join(" ") || "NONE"))
                    log(Style.fg.red, err.message);
                })
            });
        })
    };

    if (commandName.match(AhniRegExp)) {
        log(Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
        log(Style.fg.green, "User: " + message.author.username + ` [${message.author_id}] ` + " | Command: " + commandName + " | Args: " + (args?.join(" ") || "NONE"));
        if (!message.channel.nsfw) return message.channel.sendMessage("This channel is __not__ an NSFW marked channel!");
        const matched = commandName.match(AhniRegExp)
        if (!matched) return message.channel.sendMessage({ content: " ", embeds: [embed] });
        return message.channel.sendMessage({ content: "One moment..." }).then(async (m) => {
            await Ahni.nsfw(matched).then(async res => {
		console.log(res)
		const a = "SPOILER_"+res.result.toString().split("/")[7]
		const fileUp = await attach(process.env.AhniURL2 ? res.result.replace("https://kyra.tk", process.env.AhniURL2) : res.result, a)
                const embed = { media: fileUp, colour: "#00FFFF"}//, description: `[Image URL](${res.result})` }
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
        if (args.length < 5) return message.reply("Please describe your issue in more than 5 Words!")
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
//        if (!message.member.hasPermission("ManageMessages")) return message.reply("You need `Manage Messages` permission to use this command!");
        const name = message.author.username;
        const avatar = message.author.avatar;
        const content2 = await message.channel.fetchMessage(args[0])
        const content = await message.channel.fetchMessagesWithUsers(args[0])
        if (content2.channel.nsfw && !message.channel.nsfw) return message.reply("Nice try lol... that message was in an nsfw channel.")
        log(Style.fg.blue, `${Date(Date.now().toString()).slice(0, 25)}`);
        log(Style.fg.green, "User: " + message.author.username + ` [${message.author_id}] ` + " | Command: " + commandName + " | Args: " + (args?.join(" ") || "NONE"));
		const embed = { colour: "#BFDBFF", title: content2.author.username, icon_url: content2.author.generateAvatarURL({ size: 512 }), description: `[${content2.content}](https://app.revolt.chat/server/${message.channel.server._id}/channel/${content2.channel_id}/${content2._id})` };
        	//const Embed2 = new Embed().setColor("#BFDBFF").setTitle(content2.author.username).setIcon(content2.author.generateAvatarURL({ size: 512 })).setDescription(`[${content2.content}](https://app.revolt.chat/server/${message.channel.server._id}/channel/${content2.channel_id}/${content2._id})`);
		message.reply({content: " ", embeds: [Embed2]})
		console.log(embed)
	}
});

process.on("unhandledRejection", (err) => console.log(err))//log(Style.fg.red, `Heck!: ${err}`));
process.on("uncaughtException", (err) => log(Style.fg.green, `Heck: ${err}`));
process.on("warning", (err) => log(Style.fg.yellow, `${err}`));
process.on("error", (err) => console.log(err))


client.loginBot(process.env.BOT_TOKEN)
