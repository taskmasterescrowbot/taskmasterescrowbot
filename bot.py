import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

8941960635:AAHUiI_xiYpyJkxO0m7QceWr1xZPVIIeG2U = os.environ["8941960635:AAHUiI_xiYpyJkxO0m7QceWr1xZPVIIeG2U"]

ADMIN_USERNAME = "@admin"
PAYMENT_USERNAME = "@ShivamBTC"

FORM_TEXT = f"""💼 DEAL FORM 🤝

👤 Buyer:
👤 Seller:
💰 Amount:
📝 Details:

❤️ No Deal Fee
🛡️ Your Safety Is Our Priority

📣 Tag {@ShivamBTC} after submitting.

🔔 If no admin is online, send the deal amount to {PAYMENT_USERNAME} and keep a screenshot as proof. Your deal will be completed once the admin is online."""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Escrow Bot is online.\n\n"
        "Use /form to generate the deal form."
    )


async def form(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(FORM_TEXT)


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    print(f"Error: {context.error}")


def main():
    app = Application.builder().token(8941960635:AAHUiI_xiYpyJkxO0m7QceWr1xZPVIIeG2U).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("form", form))
    app.add_error_handler(error_handler)

    print("🤖 Escrow bot started...")
    app.run_polling()


if __name__ == "__main__":
    main()
