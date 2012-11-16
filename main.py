from misaka import BaseRenderer

class BBCodeRenderer(BaseRenderer):
	def block_code(self, code, language):
		if language:
			return u'\n[code=%s]%s[/code]\n' % (language, code)

		return u'\n[code]%s[/code]\n' % (code)

	def block_quote(self, quote):
		return u'[quote]%s[/quote]' % (quote)

	def block_html(self, raw_html):
		return u''

	def header(self, text, level):
		sizes = {
			1: 24,
			2: 22,
			3: 20,
			4: 18,
			5: 16
		}

		extra = {
			2: '[hr]'
		}

		values = (sizes.get(level, 16), text, extra.get(level, ''))
		return u'\n[size=%spt][b]%s[/b][/size]%s\n' % values

	def hrule(self):
		return u'[hr]'

	def list(self, contents, is_ordered):
		return u'\n[list]%s[/list]\n' % (contents)

	def list_item(self, text, is_ordered):
		return u'[li]%s[/li]' % (text)

	def paragraph(self, text):
		return u'\n%s\n' % (text)

	def table(self, header, body):
		return u'table header: %s\n[table]%s[/table]' % (header, body)

	def table_row(self, content):
		return u'[tr]%s[/tr]' % (content)

	def table_cell(self, content, flags):
		return u'[td]%s[/td]' % (content)

	def autolink(self, link, is_email):
		return u'[url=%s]%s[/url]' % (link, link)

	def codespan(self, code):
		return u'[tt]%s[/tt]' % (code)

	def double_emphasis(self, text):
		return u'[b]%s[/b]' % (text)

	def emphasis(self, text):
		return u'[i]%s[/i]' % (text)

	def image(self, link, title, alt_text):
		return u'[img]%s[/img]' % (link)

	def linebreak(self):
		return u'\n'

	def link(self, link, title, content):
		return u'[url=%s]%s[/url]' % (link, content)

	def raw_html(self, raw_html):
		return u''

	def triple_emphasis(self, text):
		return u'[u]%s[/u]' % (text)

	def strikethrough(self, text):
		return u'[s]%s[/u]' % (text)

	def superscript(self, text):
		return u'[sup]%s[/sup]' % (text)

	def entity(self, text):
		return text

	def normal_text(self, text):
		return text

	def doc_header(self):
		return u''

	def doc_footer(self):
		return u''

	def preprocess(self, full_document):
		return full_document

	def postprocess(self, full_document):
		return full_document
