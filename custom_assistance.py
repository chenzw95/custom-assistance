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
        await self.bot.delete_message(ctx.message)
        await self.simple_embed("• Autoboot SysNAND\n• Use SysNAND FIRM if booting with R\n• Show NAND or user string in System Settings\n\nIf you are configuring Luma3DS while the SD card is **not inserted** (CTRNAND Luma3DS), it is normal if you cannot see some of the above options.", title="Options to enable in Luma3DS configuration")

    @commands.command(pass_context=True)
    async def updateadv(self, ctx):
        await self.bot.delete_message(ctx.message)
        embed = discord.Embed(title="Is it safe to update?", color=discord.Color.blue())
        embed.description = "In general, it is safe to update if you have installed A9LH/CFW."
        embed.add_field(name="With CFW", value="Firmware updates with A9LH/CFW are safe. Before performing the system update, first update to the latest normal version of Luma3DS, either via the Luma Updater or by [manually downloading Luma3DS](https://github.com/AuroraWright/Luma3DS/releases) and replacing arm9loaderhax.bin on the SD card.\nYou should also repeat [section IX of the guide's last page](https://3ds.guide/installing-arm9loaderhax#section-ix---ctrnand-luma3ds) to ensure SD-less boot will work properly.")
        embed.add_field(name="Without CFW (stock firmware)", value="You are advised to consider installing CFW. For now, 11.3 is the latest firmware version where CFW installation is possible. soundhax has been patched in 11.4, and the Homebrew Launcher does not work on the O3DS at all.")
        embed.add_field(name="If you do not want to update", value="You can run [the latest version of ctr-httpwn](https://github.com/yellows8/ctr-httpwn/releases) from the Homebrew Launcher to bypass most update requirements.")
        await self.bot.say("", embed=embed)

    @commands.command(pass_context=True)
    async def updatecfw(self, ctx):
        await self.bot.delete_message(ctx.message)
        embed = discord.Embed(title="Is it safe to update if I have installed A9LH/CFW already?", color=discord.Color.blue())
        embed.description = "In general, it is safe to update if you have installed A9LH/CFW. Note, however, that ctr-httpwn has been patched in 11.4."
        embed.add_field(name="O3DS/2DS", value="If you still need the Homebrew Launcher, refer to the pinned messages in <#196635695958196224> and copy the payload file for your console to the `hblauncherloader` folder.")
        embed.add_field(name="N3DS", value="There are no issues with updating to 11.4.")
        embed.add_field(name="How to update", value="Update to the latest normal version of Luma3DS first, either via the Luma Updater or by [manually downloading Luma3DS](https://github.com/AuroraWright/Luma3DS/releases) and replacing arm9loaderhax.bin on the SD card.\nYou should also repeat [section IX of the guide's last page](https://3ds.guide/installing-arm9loaderhax#section-ix---ctrnand-luma3ds) to ensure SD-less boot will work properly.")
        await self.bot.say("", embed=embed)


def setup(bot):
    bot.add_cog(Assistance(bot))
