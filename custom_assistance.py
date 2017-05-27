import discord
from discord.ext import commands

'''Module for custom assistance commands.'''


class Assistance:

    def __init__(self, bot):
        self.bot = bot

    async def simple_embed(self, text, title="", color=discord.Color.default()):
        embed = discord.Embed(title=title, color=color)
        embed.description = text
        await self.bot.say("", embed=embed)

    @commands.command(pass_context=True)
    async def lumacfg(self, ctx):
        """Lists options to enable in Luma3DS configuration."""
        await self.bot.delete_message(ctx.message)
        embed = discord.Embed(title="Options to enable in Luma3DS configuration")
        embed.add_field(name="boot9strap", value="• Show NAND or user string in System Settings")
        embed.add_field(name="arm9loaderhax (deprecated)", value="• Autoboot SysNAND\n• Use SysNAND FIRM if booting with R\n• Show NAND or user string in System Settings\n\nIf you are configuring Luma3DS while the SD card is **not inserted** (CTRNAND Luma3DS), it is normal if you cannot see some of the above options.")
        await self.bot.say("", embed=embed)

    @commands.command(pass_context=True)
    async def updatecfw(self, ctx):
        """Firmware update advisory (CFW)"""
        await self.bot.delete_message(ctx.message)
        embed = discord.Embed(title="Is it safe to update if I have installed CFW already?", color=discord.Color.blue())
        embed.description = "In general, it is safe to update if you have installed CFW. Note, however, that ctr-httpwn has been patched in 11.4."
        embed.add_field(name="boot9strap", value="Update to the latest normal version of Luma3DS first, either via the Luma Updater or by [manually downloading Luma3DS](https://github.com/AuroraWright/Luma3DS/releases) and replacing `boot.firm` on the SD card.\nYou should also repeat [section VIII of the guide's last page](https://3ds.guide/finalizing-setup#section-viii---ctrnand-luma3ds) to ensure SD-less boot will work properly.")
        embed.add_field(name="arm9loaderhax (deprecated)", value="You should [update to boot9strap](https://3ds.guide/updating-to-boot9strap) first.")
        embed.add_field(name="Additional notes", value="If you still need the Homebrew Launcher on O3DS/2DS, refer to the pinned messages in <#196635695958196224> and copy the payload file for your console to the `hblauncherloader` folder.")
        await self.bot.say("", embed=embed)

    @commands.command(pass_context=True)
    async def safe(self, ctx):
        """Is it really safe?"""
        await self.bot.delete_message(ctx.message)
        embed = discord.Embed().set_image(url="http://i.imgur.com/X7XzvzA.png")
        await self.bot.say("", embed=embed)

    @commands.command(pass_context=True)
    async def emptysd(self, ctx):
        """Steps to repeat if SD card has been formatted"""
        await self.bot.delete_message(ctx.message)
        embed = discord.Embed(title="Blank SD card?", color=discord.Color.red())
        embed.add_field(name="boot9strap", value="Repeat the steps listed on [Finalizing setup](https://3ds.guide/finalizing-setup).")
        embed.add_field(name="arm9loaderhax (deprecated)", value="Repeat the steps listed on [Finalizing setup](https://3ds.guide/finalizing-setup), but download [Luma3DS v7.0.5](https://github.com/AuroraWright/Luma3DS/releases/tag/v7.0.5) instead of the latest release. When prompted to copy `boot.firm`, copy `arm9loaderhax.bin` instead.\n**You are advised to [update to boot9strap](https://3ds.guide/updating-to-boot9strap).**")
        await self.bot.say("", embed=embed)

    @commands.command(pass_context=True)
    async def b9s(self, ctx):
        """boot9strap information"""
        await self.bot.delete_message(ctx.message)
        embed = discord.Embed(title="What is boot9strap?", color=discord.Color.blue())
        embed.description = "boot9strap is the successor to arm9loaderhax. Luma3DS has already discontinued support for arm9loaderhax, and will require boot9strap from Luma3DS 7.1 onwards."
        embed.add_field(name="But I have been hearing this thing about sighax!", value="sighax and boot9strap work in similar ways, but the ordinary end-user **should not** attempt to use the sighax installer.")
        embed.add_field(name="How do I switch from A9LH to B9S?", value="Follow the guide to [update to boot9strap](https://3ds.guide/updating-to-boot9strap).")
        embed.add_field(name="How do I install B9S from stock?", value="Follow [the guide](https://3ds.guide).")
        await self.bot.say("", embed=embed)

    @commands.command(pass_context=True)
    async def stock114(self, ctx):
        """Advisory for users on stock 11.4 firmware"""
        await self.bot.delete_message(ctx.message)
        embed = discord.Embed(title="Regarding users on stock 11.4 firmware...", color=discord.Color.blue())
        embed.description = "To install CFW on stock 11.4 firmware, the only options available right now are to use a [DSiWare exploit](https://3ds.guide/installing-boot9strap-(dsiware\)) or by [hardmodding the console](https://3ds.guide/installing-boot9strap-(hardmod\))."
        embed.add_field(name="But these methods are so difficult!", value="You will have to wait for a kernel exploit that works on 11.4 firmware. As ordinary helpers, we cannot tell you when such an exploit will be available.")
        embed.add_field(name="Can you inform me when such an exploit is available?", value="You should either refer to <#225556031428755456> or [/r/3dshacks](https://www.reddit.com/r/3dshacks).")
        await self.bot.say("", embed=embed)

    @commands.command(pass_context=True)
    async def hardmod(self, ctx):
        """Hardmod advisory"""
        await self.bot.delete_message(ctx.message)
        embed = discord.Embed(title="What is a hardmod?", color=discord.Color.red())
        embed.description = "A hardmod involves soldering wires to specific points on the 3DS circuit board in order to read and write directly to the NAND."
        embed.add_field(name="How do I do it?", value="You should refer to the pinned messages in <#233002779717795850>.")
        embed.add_field(name="DANGER", value="Prior soldering experience is **essential**. If you make a mistake, you risk **breaking your device PERMANENTLY**.")
        await self.bot.say("", embed=embed)

    @commands.command(pass_context=True)
    async def banwave(self, ctx):
        """Ban wave advisory"""
        await self.bot.delete_message(ctx.message)
        embed = discord.Embed(title="About the ongoing ban wave...", color=discord.Color.red())
        embed.description = "A ban wave with **unknown cause** is currently ongoing. We will keep you updated (see <#225556031428755456> and <#317205045819080704>) once we obtain more information about this."
        embed.add_field(name="What happens if I have been banned?", value="As with all previous console bans, affected consoles will get error 002-0102 when attempting to play online.")
        embed.add_field(name="What should I do?", value="Please refer to <#317205045819080704>.")
        embed.add_field(name="How do I get unbanned?", value="Nintendo has stated that they will not entertain requests for unban. Server rules prevent us from assisting you in unbanning your console.")
        await self.bot.say("", embed=embed)


def setup(bot):
    bot.add_cog(Assistance(bot))
