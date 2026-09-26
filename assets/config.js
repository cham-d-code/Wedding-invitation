/* ============================================================
   SITE SETTINGS — change your brand, contact details and prices here.
   ============================================================ */
window.SITE = {
  brand: "Mangala",
  tagline: "Digital wedding invitations for Sri Lanka",
  whatsapp: "94770000000",          // your business WhatsApp number, country code first, no +
  email: "hello@yourdomain.lk",
  currency: "LKR",
  invitePath: "/i/",                // invitation links look like yourdomain.lk/i/kasun-dilini ("/api/i/" also works)
  plans: [
    { id: "classic", name: "Classic", price: 4900, note: "per wedding",
      features: ["Any of the 15 classic designs", "Unlimited guests and personal links", "RSVP dashboard with CSV export", "Countdown, maps and add-to-calendar", "Music for your tradition", "Link stays live for 6 months"] },
    { id: "premium", name: "Premium", price: 9900, note: "per wedding", featured: true,
      features: ["Everything in Classic", "All 10 premium designs", "Our story timeline and photo album", "Venue map section", "Your own music track", "Link stays live for 12 months"] },
    { id: "royal", name: "Royal", price: 19900, note: "per wedding",
      features: ["Everything in Premium", "Custom illustration of the couple", "Colours and wording tailored by our designer", "Sinhala, Tamil or English wording help", "Priority WhatsApp support", "Link stays live for 24 months"] },
  ],
};
