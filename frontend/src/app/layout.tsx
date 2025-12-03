export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-gray-50">
        <header className="p-4 border-b">
          <h1 className="text-2xl font-bold">AI Demo</h1>
        </header>
        <main className="p-6">{children}</main>
      </body>
    </html>
  );
}
