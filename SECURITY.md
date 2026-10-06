# Security

## Reporting
Found a vulnerability or evidence of tampering? Email the address on the site's "Suggest an edit" section. Please do not open a public issue for security problems.

## What protects this site
- The atlas is a single static HTML file with no user input and no cookies. The quiz adds a small server (Cloudflare Pages Functions) for payment and for the opt-in research data.
- A Content Security Policy allows scripts only from this site, connections only back to this site, and no embedding in frames (`frame-ancestors 'none'`), which stops clickjacking.
- The quiz's write endpoints accept requests only from this site's own pages. Every answer is checked against a fixed list of allowed values before it is scored or stored, and database queries use bound parameters only.
- Research data holds no names, emails, IP addresses or payment details. Raw data is readable only with the `ADMIN_TOKEN` secret; the public summary shows only aggregates of 30 or more.
- Security headers are served from `_headers` (Netlify, Cloudflare Pages) — see README for other hosts.

## The real risks
For a static site, the page itself is rarely the weak point. The plausible attacks are account takeover of the host or the domain registrar, and DNS hijacking. Mitigations live in the README checklist, not in the HTML.
