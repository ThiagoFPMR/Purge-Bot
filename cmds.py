
async def purge(message):
    """
    Executes the purge.
    """
    print("Comence the purge...")
    members = await message.guild.fetch_members(limit=200).flatten()
    print(f"Started with: {message.guild.member_count} members")
    for member in members:
        for role in member.roles:
            if role.id == 753010326840148028:
                await member.kick()
                print(f"Kicked {member.name}#{member.discriminator}")
    print(f"Finished with: {message.guild.member_count} members")