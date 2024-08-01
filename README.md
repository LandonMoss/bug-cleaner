# Bug Cleaner Discord Bot

## Description

The Bug Bounty Discord Bot is a tool designed to manage bug reports within a Discord server. It allows users to submit bugs, view their submitted bugs, and manage the status of these bugs. Administrators can assign bugs, reward users, and view all submitted bugs. The bot provides an organized way to handle bug reports and engage with users who report issues.

## Features

- **Submit Bug**: Users can submit a bug description and set a priority (low, medium, high).
- **View Bugs**: Users can view all the bugs they have submitted.
- **Search Bugs**: Users can search through their submitted bugs based on keywords.
- **Reward Bug**: Administrators can reward users for their submitted bugs.
- **Update Bug Status**: Administrators can update the status of a bug (open, in progress, closed).
- **List All Bugs**: Administrators can list all bugs submitted by all users.
- **Assign Bug**: Administrators can assign a bug to a specific user.
- **List Unassigned Bugs**: List all bugs that are not assigned to anyone.
- **Close Bug**: Users can close a bug they have submitted.
- **Edit Bug Description**: Users can update the description of a bug they have submitted.
- **Reopen Bug**: Users can reopen a bug they have previously closed.
- **List Assigned Bugs**: Users can list all bugs assigned to them.
- - **Delete Bug**: Administrators can delete specific bug reports.


## Setup

### Prerequisites

- Python 3.8 or higher
- `discord.py` library (>=2.0)
- A Discord bot token (obtainable from the [Discord Developer Portal](https://discord.com/developers/applications))

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/bug-cleaner-discord-bot.git
    cd bug-cleaner-discord-bot
    ```

2. Install the required Python packages:

    ```bash
    pip install discord.py
    ```

3. Configure your bot:

    - Open `bug.py` and replace `'YOUR_BOT_TOKEN'` with your actual Discord bot token.

4. Run the bot:

    ```bash
    python bug.py
    ```

## Usage

1. **Submit a Bug**: Use the `!submit_bug` command to start submitting a bug. The bot will ask for a description and priority.

2. **View Your Bugs**: Use the `!view_bugs` command to see the list of bugs you have submitted.

3. **Search for Bugs**: Use the `!search_bugs <keyword>` command to search for bugs based on a keyword.

4. **Close a Bug**: Use the `!close_bug <bug_id>` command to close a bug you have submitted.

5. **Edit a Bug Description**: Use the `!edit_bug_description <bug_id>` command to edit the description of a bug you have submitted.

6. **Reopen a Bug**: Use the `!reopen_bug <bug_id>` command to reopen a bug you have closed.

7. **List Assigned Bugs**: Use the `!list_assigned_bugs` command to list all bugs assigned to you.

8. **Assign a Bug** (Admin): Use the `!assign_bug <user> <bug_id>` command to assign a bug to a specific user.

9. **List Unassigned Bugs**: Use the `!list_unassigned_bugs` command to list all bugs that have not been assigned to anyone.

10. **Reward a Bug** (Admin): Use the `!reward <user> <bug_id>` command to mark a bug as rewarded.

11. **Update Bug Status** (Admin): Use the `!update_status <user> <bug_id> <status>` command to update the status of a bug (open, in progress, closed).

12. **List All Bugs** (Admin): Use the `!list_all_bugs` command to list all bugs submitted by all users.

## Contributing
