import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "AI Demo",
  description: "AI-powered chat application",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={`${inter.className} min-h-screen bg-gray-50`}>
        <header className="border-b bg-white">
          <div className="max-w-7xl mx-auto px-4 py-4">
            <h1 className="text-2xl font-bold text-gray-900">AI Demo</h1>
          </div>
        </header>
        <main>{children}</main>
      </body>
    </html>
  );
}
