"use client";

import { useState } from "react";
import Link from "next/link";

export function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav className="bg-white shadow-sm border-b">
      <div className="max-w-7xl mx-auto px-4">
        <div className="flex justify-between h-16">
          <Link href="/" className="flex items-center font-bold text-xl">
            AI Demo
          </Link>
          <button
            onClick={() => setIsOpen(!isOpen)}
            className="md:hidden p-2"
          >
            Menu
          </button>
        </div>
      </div>
    </nav>
  );
}
