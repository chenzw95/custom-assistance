import discord
from discord.ext import commands

'''Module for custom assistance commands.'''


class Assistance:

    def __init__(self, bot):
        self.bot = bot

    async def simple_embed(self, text, title="", color=discord.Color.default()):
        embed = discord.Embed(title=title, color=color)
        embed.description = text
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def module(self, ctx):
        """Lists information on the module and links to the module"""
        await ctx.message.delete()
        embed = discord.Embed(title="Chenzw's custom assistance module")
        embed.description = "Thanks for the interest in this module!"
        embed.add_field(name="What is this for?", value="This module is to help with 3DS Hacking related assistance, primarily for the Nintendo Homebrew server.")
        embed.add_field(name="Where can I download this?", value="https://github.com/chenzw95/custom-assistance")
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def lumacfg(self, ctx):
        """Lists options to enable in Luma3DS configuration."""
        await ctx.message.delete()
        embed = discord.Embed(title="Options to enable in Luma3DS configuration")
        embed.add_field(name="boot9strap", value="• Show NAND or user string in System Settings")
        embed.add_field(name="arm9loaderhax (deprecated)", value="• Autoboot SysNAND\n• Use SysNAND FIRM if booting with R\n• Show NAND or user string in System Settings\n\nIf you are configuring Luma3DS while the SD card is **not inserted** (CTRNAND Luma3DS), it is normal if you cannot see some of the above options.")
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def updatecfw(self, ctx):
        """Firmware update advisory (CFW)"""
        await ctx.message.delete()
        embed = discord.Embed(title="Is it safe to update if I have installed CFW already?", color=discord.Color.blue())
        embed.description = "That depends on which version of Luma3DS you are running (check this by holding the Select button while powering on):"
        embed.add_field(name="Luma3DS 8.0 and above (boot9strap 1.2 or newer)", value="You can update the system firmware safely. There is no pressing need to update to the latest Luma3DS, but feel free to do so.")
        embed.add_field(name="Luma3DS 7.1 (boot9strap 1.0)", value="You can update the system firmware safely. However, it is recommended that you also [update boot9strap](https://3ds.guide/updating-b9s). It does not matter whether you update b9s before or after updating the firmware. Updating b9s will also update Luma3DS automatically.\n\n**NOTE: Do not run the Luma3DS updater or replace `boot.firm` if you are on b9s 1.0. You have to follow [this guide first](https://3ds.guide/updating-b9s) in order to use the newer version of Luma3DS.**")
        embed.add_field(name="Luma3DS 7.0.5 (arm9loaderhax)", value="Updating the system firmware remains safe, but you should consider [updating to boot9strap](https://3ds.guide/a9lh-to-b9s).")
        embed.add_field(name="Any other older version", value="Assume that updating is not safe. Either download Luma3DS 7.0.5 and replace `arm9loaderhax.bin` on the SD card, or [update to boot9strap](https://3ds.guide/a9lh-to-b9s).")
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def safe(self, ctx):
        """Is it really safe?"""
        await ctx.message.delete()
        embed = discord.Embed().set_image(url="http://i.imgur.com/X7XzvzA.png")
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def emptysd(self, ctx):
        """Steps to repeat if SD card has been formatted"""
        await ctx.message.delete()
        embed = discord.Embed(title="Blank SD card?", color=discord.Color.red())
        embed.description = "Download the [Homebrew Launcher](https://github.com/fincs/new-hbmenu/releases/latest), copy `boot.3dsx` to the root of the SD card, then do one of the following depending on your console:"
        embed.add_field(name="boot9strap", value="Download the [latest compatible version](https://cdn.discordapp.com/attachments/196635695958196224/321169284124508161/compatibility_chart.png) of Luma3DS [manually from GitHub](https://github.com/AuroraWright/Luma3DS/releases), copy `boot.firm` to the root of the SD card, and repeat the steps listed on [Finalizing setup](https://3ds.guide/finalizing-setup).")
        embed.add_field(name="arm9loaderhax (deprecated)", value="Download [Luma3DS v7.0.5](https://github.com/AuroraWright/Luma3DS/releases/tag/v7.0.5), copy `arm9loaderhax.bin` to the root of the SD card, and [reinject FBI into Health & Safety](https://3ds.guide/godmode9-usage#-injecting-any-cia-app-into-health--safety).\n**You are advised to [update to boot9strap](https://3ds.guide/a9lh-to-b9s).**")
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def b9s(self, ctx):
        """boot9strap information"""
        await ctx.message.delete()
        embed = discord.Embed(title="What is boot9strap?", color=discord.Color.blue())
        embed.description = "boot9strap is the successor to arm9loaderhax. Luma3DS has already discontinued support for arm9loaderhax, and will require boot9strap from Luma3DS 7.1 onwards."
        embed.add_field(name="But I have been hearing this thing about sighax!", value="sighax and boot9strap work in similar ways, but the ordinary end-user **should not** attempt to use the sighax installer.")
        embed.add_field(name="How do I switch from A9LH to B9S?", value="Follow the guide to [update to boot9strap](https://3ds.guide/a9lh-to-b9s).")
        embed.add_field(name="How do I install B9S from stock?", value="Follow [the guide](https://3ds.guide).")
        embed.add_field(name="How do I update B9S to 1.2 from 1.0?", value="Follow the guide to [update boot9strap](https://3ds.guide/updating-b9s).")
        await ctx.send(embed=embed)

    @commands.command(pass_context=True, aliases=["stock115", "stock116"])
    async def stock114(self, ctx):
        """Advisory for users on stock 11.4+ firmware"""
        await ctx.message.delete()
        embed = discord.Embed(title="Regarding users on stock 11.4+ firmware...", color=discord.Color.blue())
        embed.description = "To install CFW on stock (unmodified) 11.4+ firmware, the only options available right now are to use [ntrboot](https://3ds.guide/ntrboot) (requires a [compatible flashcart](https://raw.githubusercontent.com/PhazonicRidley/Assistance-Links/master/Flashcard%20pic.jpg)), a [DSiWare exploit](https://3ds.guide/installing-boot9strap-(dsiware\)) (requires a second console with CFW), or by [hardmodding the console](https://3ds.guide/installing-boot9strap-(hardmod\))."
        embed.add_field(name="I am unable to use any of the above methods", value="If none of the above options are an option for you, then you will **not be able** to install custom firmware. **Downgrading is not possible.** More exploits are expected to be available only after the 3DS reaches end-of-life (EOL) status, which is predicted to be no earlier than 2019.")
        embed.add_field(name="Can you inform me when such an exploit is available?", value="You should either refer to <#225556031428755456> or [/r/3dshacks](https://www.reddit.com/r/3dshacks).")
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def hardmod(self, ctx):
        """Hardmod advisory"""
        await ctx.message.delete()
        embed = discord.Embed(title="What is a hardmod?", color=discord.Color.red())
        embed.description = "A hardmod involves soldering wires to specific points on the 3DS circuit board in order to read and write directly to the NAND."
        embed.add_field(name="How do I do it?", value="You should refer to the pinned messages in <#233002779717795850>.")
        embed.add_field(name="DANGER", value="Prior soldering experience is **essential**. If you make a mistake, you risk **breaking your device PERMANENTLY**.")
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def banwave(self, ctx):
        """Ban wave advisory"""
        await ctx.message.delete()
        embed = discord.Embed(title="About the ongoing ban wave...", color=discord.Color.red())
        embed.description = "A ban wave with **unknown cause** is currently ongoing. We will keep you updated (see <#225556031428755456>) once we obtain more information about this."
        embed.add_field(name="What happens if I have been banned?", value="As with all previous console bans, affected consoles will get error 002-0102 when attempting to play online.")
        embed.add_field(name="What should I do?", value="Please refer to <#225556031428755456>.")
        embed.add_field(name="How do I get unbanned?", value="Nintendo has stated that they will not entertain requests for unban. Server rules prevent us from assisting you in unbanning your console.")
        await ctx.send(embed=embed)

    @commands.command(pass_context=True, aliases=['lumaupdater'])
    async def nopoweron(self, ctx):
        """Advisory for users who ran the Luma updater"""
        await ctx.message.delete()
        embed = discord.Embed(title="Help! My console refuses to power on!", color=discord.Color.red())
        embed.add_field(name="I ran the Luma updater before this happened", value="Updating to Luma3DS 8.0 from any older version **also requires** an update to boot9strap. You have to revert to Luma3DS 7.1, then update B9S.")
        embed.add_field(name="I did something else", value="If the power light turns on briefly then turns back off, it means that the console could not find `boot.firm` (B9S) or `arm9loaderhax.bin` (A9LH) on your SD card.")
        embed.add_field(name="How do I fix this?", value="Download [a compatible version](https://cdn.discordapp.com/attachments/196635695958196224/321169284124508161/compatibility_chart.png) of Luma3DS, and copy the appropriate file to the root of the SD card.\n\nFor assistance with updating to B9S 1.2, please refer to [this page](https://3ds.guide/updating-b9s), or ask your question here.")
        await ctx.send(embed=embed)

    @commands.command(aliases=['ntrcfw', 'ntr'])
    async def bootntr(self, ctx):
        """Basic instructions for BootNTR selector"""
        await ctx.message.delete()
        embed = discord.Embed(title="How do I use NTR CFW?", color=discord.Color.blue())
        embed.description = "BootNTR **selector** is recommended for launching NTR. It can be downloaded [here](https://github.com/Nanquitas/BootNTR/releases)."
        embed.add_field(name="N3DS", value="Choose one of the **non-mode3** variants. The choice of banner is purely a matter of preference.")
        embed.add_field(name="O3DS",
                        value="Choose the non-mode3 variant. If you intend to use NTR with an extended memory game (eg. Smash, generation VII Pokemon), then you will need the **mode3** variant instead. The choice of banner is purely a matter of preference.")
        embed.add_field(name="Take note!", value="NTR CFW is not a CFW in itself, and requires Luma3DS to work. Streaming works only from N3DS/N2DS.")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Assistance(bot))
