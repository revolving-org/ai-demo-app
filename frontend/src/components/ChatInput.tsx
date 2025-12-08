"use client";

import { useState } from "react";

export function ChatInput() {
  const [message, setMessage] = useState("");

  return (
    <div className="border-t p-4">
      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        className="w-full border rounded-lg p-3"
        placeholder="Type your message..."
      />
    </div>
  );
}
