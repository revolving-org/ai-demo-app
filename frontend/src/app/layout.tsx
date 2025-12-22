import { Navbar } from "@/components/Navbar";
import "./globals.css";

export const metadata = {
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
      <body className="min-h-screen bg-gray-50">
        <Navbar />
        <main>{children}</main>
      </body>
    </html>
  );
}
