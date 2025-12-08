import { ChatInput } from "@/components/ChatInput";
import { MessageList } from "@/components/MessageList";

export default function ChatPage() {
  return (
    <div className="flex flex-col h-screen">
      <MessageList />
      <ChatInput />
    </div>
  );
}
