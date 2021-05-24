from amigo.models import Chat, ChatStatus, User, Participation, ModelManager
from amigo.views.base import BaseView


class OrganizeView(BaseView):

    @classmethod
    def info(cls):
        return "message", {"commands": ["organize", ]}

    def group(self, message):
        chat_member = self.bot.get_chat_member(chat_id=message.chat.id,
                                               user_id=message.from_user.id)
        is_admin = chat_member.status == 'administrator' or \
                   chat_member.status == 'creator'

        if not is_admin:
            self.bot.reply_to(message, "You don't have access to this command")
            return

        user = ModelManager(self.db, User).get_object(filter={
            "telegram_id": message.from_user.id
        })

        if not user:
            self.bot.reply_to(message, "You are not start me in private chat")
            return

        chat = ModelManager(self.db, Chat).get_object(filter={
            "telegram_id": message.chat.id
        })

        if not chat:
            self.bot.reply_to(message, "Chat is not started")
            return

        if chat.organizer is not None and chat.organizer.telegram_id == user.telegram_id:
            self.bot.reply_to(message, "Okay, you are not an organizer now.")
            ModelManager(self.db, Chat).update_obj(
                obj=chat,
                values={
                    "organizer": None
                }
            )
            return
        ModelManager(self.db, Chat).update_obj(
            obj=chat,
            values={
                "organizer": user
            }
        )
        self.bot.reply_to(message, "Okay, you are an organizer now.")

    def private(self, message):
        self.bot.reply_to(message, "This command works only in groups")
