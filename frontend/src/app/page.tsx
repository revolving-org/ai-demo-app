import Link from "next/link";

export default function Home() {
  return (
    <div className="max-w-7xl mx-auto px-4 py-12">
      <section className="text-center mb-16">
        <h2 className="text-4xl font-bold text-gray-900 mb-4">
          Chat with AI
        </h2>
        <p className="text-xl text-gray-600 mb-8">
          Experience the power of conversational AI
        </p>
        <Link
          href="/chat"
          className="bg-indigo-600 text-white px-8 py-3 rounded-lg font-medium hover:bg-indigo-700"
        >
          Start Chatting
        </Link>
      </section>

      <section className="grid md:grid-cols-3 gap-8">
        {["Fast", "Secure", "Smart"].map((feature) => (
          <div key={feature} className="bg-white p-6 rounded-lg shadow-sm">
            <h3 className="font-semibold text-lg mb-2">{feature}</h3>
            <p className="text-gray-600">
              Built with the latest technology stack.
            </p>
          </div>
        ))}
      </section>
    </div>
  );
}
